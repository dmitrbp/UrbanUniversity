from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        data = file.readline()
        while data:
            all_data.append(data)
            data = file.readline()


all_files = [f'./file {number}.txt' for number in range(1, 5)]

MULTIPROCCESSING = True

if not MULTIPROCCESSING:
    start = datetime.now()
    for file in all_files:
        read_info(file)
    end = datetime.now()
    print(f'{end - start} (линейный)')
if MULTIPROCCESSING and __name__ == '__main__':
    start = datetime.now()
    with Pool(4) as p:
        p.map(read_info, all_files)
    end = datetime.now()
    print(f'{end - start} (многопроцессорный)')
