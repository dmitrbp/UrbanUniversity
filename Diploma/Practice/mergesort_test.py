import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from multiprocessing import Manager, Pool
import matplotlib.pyplot as plt
import asyncio


class Timer:
    """
    Класс для подсчета длительности вычислительных операций
    """
    def __init__(self, *steps):
        """
        Конструктор класса
        :param steps: Имена шагов (ключи словаря), для записи и чтения данных по длительности
        """
        self._time_per_step = dict.fromkeys(steps)

    def __getitem__(self, item):
        """
        Магический метод получения значения по ключу
        :param item: значение ключа (имя шага измерения)
        :return: значение из словаря (длительность операции)
        """
        return self.time_per_step[item]

    @property
    def time_per_step(self):
        """
        Свойство для чтения элементов словаря
        :return: значение длительности операции
        """
        return {
            step: elapsed_time
            for step, elapsed_time in self._time_per_step.items()
            if elapsed_time is not None and elapsed_time > 0
        }

    def start_for(self, step):
        """
        Запуск таймера для определенного шага
        :param step: шаг
        :return: None
        """
        self._time_per_step[step] = -time.time()

    def stop_for(self, step):
        """
        Остановка таймера для определенного шага
        :param step: шаг
        :return: None
        """
        self._time_per_step[step] += time.time()


def merge_sort_multiple(results, array):
    """
    Функция сортировки для многопроцессорной обработки
    :param results: массив для агрегирования результатов
    :param array: сортируемый массив
    :return: None
    """
    results.append(merge_sort(array))


def merge_multiple(results, array_part_left, array_part_right):
    """
    Функция слияния результатов для многопроцессорной обработки
    :param results: массив для агрегирования результатов
    :param array_part_left: левый массив для слияния
    :param array_part_right: правый массив для слияния
    :return: None
    """
    results.append(merge(array_part_left, array_part_right))


def merge_sort(array):
    """
    Функция сортировки для одного потока выполнения
    :param array: сортируемый массив
    :return: отсортированный массив
    """
    array_length = len(array)

    if array_length <= 1:
        return array

    middle_index = int(array_length / 2)
    left = array[0:middle_index]
    right = array[middle_index:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def thread_merge_sort(array, level = 0):
    """
    Функция сортировки для многопотоковой обработки
    :param array: сортируемый массив
    :param level: глубина сортировки, начиная с которой вызывается однопоточная сортировка.
    До этого уровня вызывается многопоточная
    :return: отсортированный массив
    """
    level += 1
    array_length = len(array)
    if array_length <= 1:
        return array

    middle_index = int(array_length / 2)
    left = array[0:middle_index]
    right = array[middle_index:]
    with ThreadPoolExecutor() as executor:
        if level > 1:
            future1 = executor.submit(thread_merge_sort, (left, level, ))
            future2 = executor.submit(thread_merge_sort, (right, level, ))
        else:
            future1 = executor.submit(merge_sort, left)
            future2 = executor.submit(merge_sort, right )
        left = future1.result()
        right = future2.result()
    return merge(left, right)

async def async_merge_sort(array):
    """
    Функция сортировки для корутинной (asyncio) обработки
    :param array: сортируемый массив
    :return: отсортированный массив
    """
    array_length = len(array)
    if array_length <= 1:
        return array

    middle_index = int(array_length / 2)
    left = array[0:middle_index]
    right = array[middle_index:]
    task_left = async_merge_sort(left)
    task_right = async_merge_sort(right)
    # left = await async_merge_sort(left)
    # right = await async_merge_sort(right)
    left, right = await asyncio.gather(task_left, task_right)
    return merge(left, right)

def merge(left, right):
    """
    Функция однопоточного слияния двух массивов
    :param left: левый массив
    :param right: правый массив
    :return: массив после слияния правой и левой частей
    """
    sorted_list = []
    # Создаем копии, чтобы не изменять
    # оригинальные объекты.
    left = left[:]
    right = right[:]
    # На самом деле не нужно проверять длину списков,
    # так как истинность пустых списков равна False.
    # Это сделано для демонстрации алгоритма.
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        elif len(left) > 0:
            sorted_list.append(left.pop(0))
        elif len(right) > 0:
            sorted_list.append(right.pop(0))
    return sorted_list

@contextmanager
def process_pool(size):
    """
    Создаем пул процессов и блокируем его до тех пор, пока все процессы не завершатся.
    :param size: размер пула
    :return: None
    """
    pool = Pool(size)
    yield pool
    pool.close()
    pool.join()

def parallel_merge_sort(array, process_count):
    """
    Основная функция многопроцессорной сортировки
    :param array: сортируемый массив
    :param process_count: количество процессоров, задействованных в сортировке
    :return: отсортированный массив
    """
    # Делим список на части
    step = int(length / process_count)

    # Используется объект multiprocessing.Manager, для хранения вывода каждого процесса.
    # Пример здесь:
    # http://docs.python.org/library/multiprocessing.html#sharing-state-between-processes
    manager = Manager()
    results = manager.list()

    with process_pool(size=process_count) as pool:
        for n in range(process_count):
            # Создаем новый объект Process и присваиваем ему
            # значение, возвращаемое функцией merge_sort_multiple,
            # использую подсписок, как входное значение
            if n < process_count - 1:
                chunk = array[n * step : (n + 1) * step]
            else:
                # Оставшиеся элементы - в список
                chunk = array[n * step:]
            pool.apply_async(merge_sort_multiple, (results, chunk))

    # Слияние:
    # При количестве ядер больше 2 мы можем использовать мультипроцессинг
    # для параллельного слияния подсписков.
    while len(results) > 1:
        with process_pool(size=process_count) as pool:
            pool.apply_async(
                merge_multiple,
                (results, results.pop(0), results.pop(0))
            )

    final_sorted_list = results[0]

    return final_sorted_list


if __name__ == '__main__':
    # Подготовка данных для графического отображения
    x  = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    for length in range(20000, 200001, 20000):
        x.append(length)
        print('-- Размер сортируемого массива - {:,}'.format(length).replace(',',' '))

        main_timer = Timer('sync', 'thread', 'async', '2_core', '4_core')

        # Создание разреженного массива для более интенсивной сортировки
        unsorted_array = [i if i % 2 else length - i for i in range(length, 0, -1)]
        # Создаение отсортированной копии для сравнения
        sorted_array_etalon = unsorted_array[:]
        sorted_array_etalon.sort()

        # Сортировка

        # Запуск синхронной сортировки
        main_timer.start_for('sync')
        sorted_array = merge_sort(unsorted_array)
        main_timer.stop_for('sync')
        # Сравнение с эталонным массовом для проверки правильности реализации.
        if sorted_array_etalon == sorted_array:
            print('Время синхронной сортировки: %4.6f sec' % main_timer['sync'])
        else:
            print('SyncSort: Отсортированный массив не совпадает с эталонным')
            break

        # Запуск потоковой сортировки
        main_timer.start_for('thread')
        sorted_array = thread_merge_sort(unsorted_array)
        main_timer.stop_for('thread')
        if sorted_array_etalon == sorted_array:
            print('Время потоковой сортировки: %4.6f sec' % main_timer['thread'])
        else:
            print('ThreadSort: Отсортированный массив не совпадает с эталонным')
            break

        # Запуск корутинной сортировки
        main_timer.start_for('async')
        sorted_array = asyncio.run(async_merge_sort(unsorted_array))
        main_timer.stop_for('async')
        if sorted_array_etalon == sorted_array:
            print('Время корутинной сортировки: %4.6f sec' % main_timer['async'])
        else:
            print('AsyncSort: Отсортированный массив не совпадает с эталонным')
            break

        # Запуск 2-х процессорной сортировки
        main_timer.start_for('2_core')
        sorted_array = parallel_merge_sort(unsorted_array, 2)
        main_timer.stop_for('2_core')
        if sorted_array_etalon == sorted_array:
            print('Время 2-х процессорной сортировки: %4.6f sec' % main_timer['2_core'])
        else:
            print('2-CoreSort: Отсортированный массив не совпадает с эталонным')
            break

        # Запуск 4-х процессорной сортировки
        main_timer.start_for('4_core')
        sorted_array = parallel_merge_sort(unsorted_array, 4)
        main_timer.stop_for('4_core')
        if sorted_array_etalon == sorted_array:
            print('Время 4-х процессорной сортировки: %4.6f sec' % main_timer['4_core'])
        else:
            print('4-CoreSort: Отсортированный массив не совпадает с эталонным')
            break

        # Сохранение графических результатов
        y1.append((main_timer['sync']))
        y2.append((main_timer['thread']))
        y3.append((main_timer['async']))
        y4.append((main_timer['2_core']))
        y5.append((main_timer['4_core']))

    # Вывод графических результатов
    plt.title('Сравнение времени сортировки слиянием')
    plt.xlabel('Размер массива (элементов)')
    plt.ylabel('Время выполнения (сек)')
    plt.plot(x, y1, label='Sync', linestyle='solid')
    plt.plot(x, y2, label='Thread', linestyle='dashed')
    plt.plot(x, y3, label='Async', linestyle='dotted')
    plt.plot(x, y4, label='2-Core', linestyle='solid')
    plt.plot(x, y5, label='4-Core', linestyle='dashdot')
    plt.legend()
    plt.grid(True, which='both', linestyle='--')
    plt.show()
