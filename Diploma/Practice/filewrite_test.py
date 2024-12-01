import asyncio
import matplotlib.pyplot as plt

from filewrite_classes import AsyncTester, ThreadTester

async def async_tester(files_count, file_size):
    writter = await AsyncTester(files_count, file_size)
    result = await writter.run()
    print (
        f'Asyncio: размер файла - {result[0]}, '
        f'время выполнения - {result[1]:.2f}, '
        f'потоков - {result[2]}'
    )
    return result

def thread_tester(files_count, file_size):
    writter = ThreadTester(files_count, file_size)
    result = writter.run()
    print (
        f'Threads: размер файла - {result[0]}, '
        f'время выполнения - {result[1]:.2f}, '
        f'потоков - {result[2]}'
    )
    return result

files_count = 10
file_size = 2000000
# results = []
x = []
y1 = []
y2 = []
for f_size in range(1000000, 2000001, 250000):
    async_result = asyncio.run(async_tester(files_count, f_size))
    thread_result = thread_tester(files_count, f_size)
    # results.append(async_result)
    # results.append(thread_result)
    x.append(f_size)
    y1.append((async_result[1], thread_result[1]))
    y2.append((async_result[1], thread_result[1]))
plt.title('Сравнение времени записи/чтения файлов для AsyncIO и Threads')
plt.xlabel('Размер файла (Mb)')
plt.ylabel('Время выполнения (сек)')
plt.plot(x, y1, label = 'AsyncIO', linestyle='-')
plt.plot(x, y2, label = 'Threads', linestyle='--')
plt.legend()
plt.grid()
plt.show()
