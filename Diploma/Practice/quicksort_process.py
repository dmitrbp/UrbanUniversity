import sys
import time
import threading
from multiprocessing.pool import Pool
import concurrent.futures
import random


def partition(nums, low, high):
    i = low - 1
    pivot = nums[high]

    for j in range(low, high):
        if nums[j] <= pivot:
            i = i + 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def quick_sort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)

        # Create two processes to sort the two halves of the array concurrently
        # with Pool() as p:
        #     result = p.map_async(func=quick_sort, iterable=[(nums, low, pi - 1, ), (nums, pi + 1, high, )])
        #     result.wait()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future1 = executor.submit(quick_sort, nums, low, pi - 1)
            future2 = executor.submit(quick_sort, nums, pi + 1, high)
            # result1 = future1.result()
            # result2 = future2.result()



# Example usage
if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    arr_length = 10000
    # arr = [i if i % 2 else arr_length - i for i in range(arr_length, 0, -1)]
    arr = [random.randint(0, n * 100) for n in range(arr_length)]
    # print("Original array:", arr)
    start_time = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    # print("Sorted array:", arr)
    print(f'Elapsed: {time.time() - start_time}')