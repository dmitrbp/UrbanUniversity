import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    print('--- Соревнования начаты')

    tasks = []
    tasks.append(asyncio.create_task(start_strongman('Pasha', 3)))
    tasks.append(asyncio.create_task(start_strongman('Denis', 4)))
    tasks.append(asyncio.create_task(start_strongman('Apollon', 5)))

    # await asyncio.gather(*tasks)
    for task in tasks:
        await task

    print('--- Соревнования закончены')


asyncio.run(start_tournament())
