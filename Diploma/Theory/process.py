from multiprocessing.pool import Pool
import time

maxnumber = 10

def worker(number):
    sleep = maxnumber - number
    time.sleep(sleep)
    print("I am Worker {}, I slept for {} seconds".format(number, sleep))


if __name__ == '__main__':
    start_time = time.time()
    with Pool() as p:
        res = p.map_async(worker, range(maxnumber))
        print("All Processes are queued, let's see when they finish!")
        res.wait()
    print("Async is finished. Elapced:", time.time() - start_time)

