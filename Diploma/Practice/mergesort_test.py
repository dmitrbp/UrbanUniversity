from concurrent.futures import ThreadPoolExecutor
import time
from contextlib import contextmanager
from multiprocessing import Manager, Pool
import matplotlib.pyplot as plt


class Timer():
    def __init__(self, *steps):
        self._time_per_step = dict.fromkeys(steps)

    def __getitem__(self, item):
        return self.time_per_step[item]

    @property
    def time_per_step(self):
        return {
            step: elapsed_time
            for step, elapsed_time in self._time_per_step.items()
            if elapsed_time is not None and elapsed_time > 0
        }

    def start_for(self, step):
        self._time_per_step[step] = -time.time()

    def stop_for(self, step):
        self._time_per_step[step] += time.time()


def merge_sort_multiple(results, array):
    results.append(merge_sort(array))


def merge_multiple(results, array_part_left, array_part_right):
    results.append(merge(array_part_left, array_part_right))


def merge_sort(array):
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

def merge(left, right):
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
    Создаем пул процессов и блокируйте его до тех пор, пока все процессы не завершатся.
    """
    pool = Pool(size)
    yield pool
    pool.close()
    pool.join()


def parallel_merge_sort(array, process_count):
    # Делим список на части
    step = int(length / process_count)

    # Используется объект multiprocessing.Manager, для
    # хранения вывода каждого процесса.
    # См. пример здесь
    # http://docs.python.org/library/multiprocessing.html#sharing-state-between-processes
    manager = Manager()
    results = manager.list()

    with process_pool(size=process_count) as pool:
        for n in range(process_count):
            # Создаем новый объект Process и присваиваем ему
            # значение, возвращаемое функцией merge_sort_multiple,
            # использую подсписок, как входное значение
            if n < process_count - 1:
                chunk = array[n * step:(n + 1) * step]
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
    x = []
    y = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for length in range(20000, 200001, 20000):
        x.append(length)
        print('-- Размер сортируемого массива - {:,}'.format(length).replace(',',' '))

        main_timer = Timer('sync', 'thread', '2_core', '4_core')

        # Создание массива для сортировки
        # randomized_array = [random.randint(0, n * 100) for n in range(length)]
        unsorted_array = [i if i % 2 else length - i for i in range(length, 0, -1)]
        # Создаение отслртированной копии для сравнения
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

        y1.append((main_timer['sync']))
        y2.append((main_timer['thread']))
        y3.append((main_timer['2_core']))
        y4.append((main_timer['4_core']))
    plt.title('Сравнение времени сортировки слиянием')
    plt.xlabel('Размер массива (элементов)')
    plt.ylabel('Время выполнения (сек)')
    plt.plot(x, y1, label='Sync', linestyle='-')
    plt.plot(x, y2, label='Thread', linestyle=':')
    plt.plot(x, y3, label='2-Core', linestyle='--')
    plt.plot(x, y4, label='4-Core', linestyle='-.')

    plt.legend()
    plt.grid(True, which='both', linestyle='--')
    plt.show()
