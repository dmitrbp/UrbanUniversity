import threading
import time

start_time = time.time()
maxnumber = 10

def worker(number):
    sleep = maxnumber - number
    time.sleep(sleep)
    print("I am Worker {}, I slept for {} seconds".format(number, sleep))


#------------- Async -------------
print("Async is started, let's see when it finish!")
threads = []
for i in range(maxnumber):
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()
    threads.append(thread)

print("All Threads are queued")

for thread in threads:
    thread.join()

print("Async is finished. Elapced:", time.time() - start_time)
#------------- Sync -------------
print("Sync is started, let's see when it finish!")

start_time = time.time()
for i in range(maxnumber):
    worker(i)

print("Sync is finished. Elapced:", time.time() - start_time)