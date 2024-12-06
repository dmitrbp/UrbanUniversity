import asyncio
import random
import threading
import time
import aiofiles
from async_class import AsyncClass
from collections import namedtuple



TestResult = namedtuple('TestResult', ['file_size', 'elapsed_time', 'threads_count'])

class AsyncTester(AsyncClass):
    async def __ainit__(self, files_count, file_size):
        """
        Конструктор класса
        :param files_count: количество файлов для тестирования
        :param file_size: размер каждого файлов в байтах
        :return: класс
        """
        self.files_count = files_count
        self.file_size = file_size

    async def run(self):
        """
        Функция асинхронного тестирования
        :return: результаты тестирования в виде именованного кортежа
        """
        write_tasks = []
        read_tasks = []
        start_time = time.time()
        for i in range(self.files_count):
            write_tasks.append(self.writter(f'{i}.txt'))
        for i in range(self.files_count * 100):
            read_tasks.append(self.reader(self.files_count))
        threads_count = threading.active_count()
        await asyncio.gather(*write_tasks)
        await asyncio.gather(*read_tasks)
        return TestResult(self.file_size, (time.time() - start_time), threads_count)

    async def writter(self, filename):
        """
        Функция записи в файл
        :param filename: имя файла
        :return: None
        """
        async with aiofiles.open(filename, mode='w') as file:
            content = ''.join([str(num) for num in range(self.file_size)])
            await file.write(content)

    async def reader(self, files_count):
        """
        Функция чтения из случайного файла в пределах предварительно созданных
        :param files_count: количество файлов
        :return: None
        """
        i = random.randint(0, files_count - 1)
        async with aiofiles.open(f'{i}.txt', mode='r') as file:
            await asyncio.sleep(random.uniform(0, 2))
            await file.read()


class ThreadTester:
    def __init__(self, files_count, file_size):
        """
        Конструктор класса
        :param files_count: количество файлов
        :param file_size: размер каждого файла в байтах
        """
        self.files_count = files_count
        self.file_size = file_size

    def run(self):
        """
        Функция потокового тестирования
        :return: результаты тестирования в виде именованного кортежа
        """
        write_threads = []
        read_threads = []
        start_time = time.time()
        # write files
        for i in range(self.files_count):
            thread = threading.Thread(target=self.writter, args=[i])
            thread.start()
            write_threads.append(thread)
        threads_count = threading.active_count()
        # read files with sleep
        for thread in write_threads:
            thread.join()
        for i in range(self.files_count * 100):
            thread = threading.Thread(target=self.reader, args=[self.files_count])
            thread.start()
            read_threads.append(thread)
        threads_count = max(threads_count, threading.active_count())
        for thread in read_threads:
            thread.join()
        return TestResult(self.file_size, (time.time() - start_time), threads_count)

    def writter(self, i):
        """
        Функция записи в файл
        :param i: номер файла
        :return: None
        """
        with open(f'{i}.txt', mode='w') as file:
            content = ''.join([str(num) for num in range(self.file_size)])
            file.write(content)

    def reader(self, files_count):
        """
        Функция чтения из случайного файла в пределах предварительно созданных
        :param files_count: количество файлов
        :return:
        """
        i = random.randint(0, files_count - 1)
        with open(f'{i}.txt', mode='r') as file:
            time.sleep(random.uniform(0, 2))
            file.read()
