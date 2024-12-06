import asyncio
import matplotlib.pyplot as plt
from filewrite_classes import *
from collections import namedtuple


async def async_tester(files_count, file_size):
    """
    Функция одиночного асинхронного тестирования
    :param files_count: количество файлов
    :param file_size: размер каждого файла
    :return:
    """
    writter = await AsyncTester(files_count, file_size)
    result = await writter.run()
    print (
        f'Asyncio: размер файла - {result[0]}, '
        f'время выполнения - {result[1]:.2f}, '
        f'потоков - {result[2]}'
    )
    return result

def thread_tester(files_count, file_size):
    """
    Функция одиночного потокового тестирования
    :param files_count: количество файлов
    :param file_size: размер каждого файла
    :return:
    """
    writter = ThreadTester(files_count, file_size)
    result = writter.run()
    print (
        f'Threads: размер файла - {result[0]}, '
        f'время выполнения - {result[1]:.2f}, '
        f'потоков - {result[2]}'
    )
    return result

# Количество файлов для тестирования
files_count = 10
# Списки для построения графиков
x = []
y1 = []
y2 = []
# Цикл тестирования для разных размеров файлов
for f_size in range(100000, 200001, 25000):
    async_result = asyncio.run(async_tester(files_count, f_size))
    thread_result = thread_tester(files_count, f_size)
    x.append(f_size / 1000000)
    y1.append(async_result.elapsed_time)
    y2.append(thread_result.elapsed_time)
# Отображение результатов на графике
plt.title('Сравнение времени записи/чтения файлов для AsyncIO и Threads')
plt.xlabel('Размер файла (Mb)')
plt.ylabel('Время выполнения (сек)')
plt.plot(x, y1, label = 'AsyncIO', linestyle='-')
plt.plot(x, y2, label = 'Threads', linestyle='--')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.show()
