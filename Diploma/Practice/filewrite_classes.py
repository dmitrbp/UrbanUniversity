import asyncio
import aiofiles
import time
import threading
from async_class import AsyncClass, AsyncObject, task, link

class AsyncTester(AsyncClass):
    async def __ainit__(self, files_count, file_size):
        self.files_count = files_count
        self.file_size = file_size

    async def run(self):
        tasks = []
        start_time = time.time()
        for i in range(self.files_count):
            tasks.append(self.writter(f'{i}.txt'))
            tasks.append(self.reader(f'{i}.txt'))
        threads_count = threading.active_count()
        await asyncio.gather(*tasks)
        return (self.file_size, (time.time() - start_time), threads_count)

    async def writter(self, filename):
        async with aiofiles.open(filename, mode='w') as file:
            content = ''.join([str(num) for num in range(self.file_size)])
            await file.write(content)

    async def reader(self, filename):
        async with aiofiles.open(filename, mode='r') as file:
            content = await file.readlines()


class ThreadTester():
    def __init__(self, files_count, file_size):
        self.files_count = files_count
        self.file_size = file_size

    def run(self):
        threads = []
        start_time = time.time()
        for i in range(self.files_count):
            thread = threading.Thread(target=self.writter, args=[i])
            thread.start()
            threads.append(thread)
            thread = threading.Thread(target=self.reader, args=[i])
            thread.start()
            threads.append(thread)
        threads_count = threading.active_count()
        for thread in threads:
            thread.join()
        return (self.file_size, (time.time() - start_time), threads_count)

    def writter(self, i):
        with open(f'{i}.txt', mode='w') as file:
            content = ''.join([str(num) for num in range(self.file_size)])
            file.write(content)

    def reader(self, i):
        with open(f'{i}.txt', mode='r') as file:
            content = file.readlines()
