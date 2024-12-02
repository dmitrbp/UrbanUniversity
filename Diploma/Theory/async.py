import asyncio
import time


maxnumber = 5

async def worker(number):
    sleep = maxnumber - number
    await asyncio.sleep(sleep)
    print("Рабочий процесс {}, засыпание на {} сек.".format(number, sleep))

async def run():
    print("Асинхронный корутинный процесс стартовал")
    start_time = time.time()
    tasks = []
    for i in range(maxnumber):
        tasks.append(worker(i))

    print("Все корутины запущены, ожидаем завершения")
    await asyncio.gather(*tasks)

    print("Асинхронный корутинный процесс завершен. Затрачено: {} сек".format(time.time() - start_time))

asyncio.run(run())