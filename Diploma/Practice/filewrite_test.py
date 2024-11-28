import threading
import aiofiles
import asyncio
import time

async def async_writter():
    tasks = []
    start_time = time.time()
    for i in range(10):
        tasks.append(writter1(i))
    await asyncio.gather(*tasks)
    print(f'Asyncio elapsed: {time.time() - start_time}, threads: {threading.active_count()}')

async def writter1(i):
    async with aiofiles.open(f'{i}.txt', mode='w+') as file:
        content = ''.join([str(num) for num in range(1000000)])
        await file.write(content)
        await file.readlines()
        # await asyncio.sleep(3)

def thread_writter():
    threads = []
    start_time = time.time()
    for i in range(10):
        thread = threading.Thread(
            target=writter2,
            args = [i]
        )
        thread.start()
        threads.append(thread)
    threads_count = threading.active_count()
    for thread in threads:
        thread.join()
    print(f'Threads elapsed: {time.time() - start_time}, threads: {threads_count}')


def writter2(i):
    with open(f'{i}.txt', mode='w+') as file:
        content = ''.join([str(num) for num in range(1000000)])
        file.write(content)
        file.readlines()
        # time.sleep(3)

asyncio.run(async_writter())
thread_writter()