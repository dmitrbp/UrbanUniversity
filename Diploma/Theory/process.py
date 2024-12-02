from multiprocessing.pool import Pool
import time


maxnumber = 5

def worker(number):
    sleep = maxnumber - number
    time.sleep(sleep)
    print("Рабочий процесс {}, засыпание на {} сек.".format(number, sleep))


if __name__ == '__main__':
    start_time = time.time()
    print("Мультипроцессорный код стартовал ")
    with Pool() as p:
        res = p.map_async(worker, range(maxnumber))
        print("Все процессы запущены, ожидаем завершения")
        res.wait()
    print("Мультипроцесоорный код завершен. Затрачено:{} сек".format(time.time() - start_time))

