import time


maxnumber = 5

def worker(number):
    sleep = maxnumber - number
    time.sleep(sleep)
    print("Рабочий процесс {}, засыпание на {} сек.".format(number, sleep))

print("Синхронный процесс стартовал")
start_time = time.time()
for i in range(maxnumber):
    worker(i)

print("Синхронный процесс завершен. Затрачено: {} сек".format(time.time() - start_time))