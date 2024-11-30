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

def thread_merge_sort(array):
    array_length = len(array)
    if array_length <= 1:
        return array

    middle_index = int(array_length / 2)
    left = array[0:middle_index]
    right = array[middle_index:]
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(merge_sort, left)
        future2 = executor.submit(merge_sort, right)
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
    xlist = []
    ylist = []
    for length in range(100000, 200001, 25000):
        xlist.append(length)
        print('Размер сортируемого массива - {:,}'.format(length).replace(',',' '))

        main_timer = Timer('sync', 'thread', '2_core', '4_core')

        # Создание массива для сортировки
        # randomized_array = [random.randint(0, n * 100) for n in range(length)]
        unsorted_array = [i if i % 2 else length - i for i in range(length, 0, -1)]

        # Сортировка

        print('-- Запуск синхронной сортировки')
        main_timer.start_for('sync')
        sorted_array = merge_sort(unsorted_array)
        main_timer.stop_for('sync')
        # Создаение копии для предотвращения многопоточной интерференции
        sorted_array_etalon = unsorted_array[:]
        sorted_array_etalon.sort()
        # Сравнение с методом сортировки списков Python (sort),
        # служит для проверки правильности реализации.
        print('Проверка отсортированного массова:', sorted_array_etalon == sorted_array)
        print('Время синхронной сортировки: %4.6f sec' % main_timer['sync'])

        print('-- Запуск потоковой сортировки')
        main_timer.start_for('thread')
        thread_sorted_array = thread_merge_sort(unsorted_array)
        main_timer.stop_for('thread')
        print('Проверка отсортированного массова:', sorted_array_etalon == thread_sorted_array)
        print('Время потоковой сортировки: %4.6f sec' % main_timer['thread'])

        print('-- Запуск 2-х процессорной сортировки')
        main_timer.start_for('2_core')
        parallel_sorted_array = parallel_merge_sort(unsorted_array, 2)
        main_timer.stop_for('2_core')
        print('Проверка отсортированного массова:', sorted_array_etalon == parallel_sorted_array)
        print('Время 2-х процессорной сортировки: %4.6f sec' % main_timer['2_core'])

        print('-- Запуск 4-х процессорной сортировки')
        main_timer.start_for('4_core')
        parallel_sorted_array = parallel_merge_sort(unsorted_array, 4)
        main_timer.stop_for('4_core')
        print('Проверка отсортированного массова:', sorted_array_etalon == parallel_sorted_array)
        print('Время 4-х процессорной сортировки: %4.6f sec' % main_timer['4_core'])

        ylist.append((main_timer['sync'], main_timer['thread'], main_timer['2_core'], main_timer['4_core']))
    plt.title('Сравнение времени сортировки слиянием')
    plt.xlabel('Размер мвссива (элементов)')
    plt.ylabel('Время выполнения (сек)')
    plt.plot(xlist, ylist, label=('Sync', 'Threads', '2-core', '4-core'))
    plt.legend()
    plt.grid()
    plt.show()
