import asyncio
import datetime
import random


async def sleep_func():
    await asyncio.sleep(random.randint(0, 5))

async def display_date(num, loop):
    end_time = loop.time() + 10.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await sleep_func()

async def main():
    t1 = loop.create_task(display_date(2, loop))
    t2 = loop.create_task(display_date(3, loop))
    await asyncio.wait([t1, t2])


loop = asyncio.get_event_loop()
asyncio.ensure_future(display_date(4, loop))
asyncio.ensure_future(display_date(5, loop))

asyncio.run(display_date(1, loop))
loop.run_until_complete(main())