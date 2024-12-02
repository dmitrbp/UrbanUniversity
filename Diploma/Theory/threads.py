import threading
import time


maxnumber = 5

def worker(number):
    sleep = maxnumber - number
    time.sleep(sleep)
    print("Рабочий процесс {}, засыпание на {} сек.".format(number, sleep))

print("Асинхронный поточный процесс стартовал")
start_time = time.time()
threads = []
for i in range(maxnumber):
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()
    threads.append(thread)

print("Все потоки запущены, ожидаем завершения")
for thread in threads:
    thread.join()

print("Асинхронный поточный процесс завершен. Затрачено: {} сек".format(time.time() - start_time))
