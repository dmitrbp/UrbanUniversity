import random
import sys
import time
import threading


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

        # Create two threads to sort the two halves of the array concurrently
        left_thread = threading.Thread(target=quick_sort, args=(nums, low, pi - 1))
        right_thread = threading.Thread(target=quick_sort, args=(nums, pi + 1, high))

        # Start the threads
        left_thread.start()
        right_thread.start()

        # Wait for both threads to finish
        left_thread.join()
        right_thread.join()


# Example usage
# sys.setrecursionlimit(100000)
arr_length = 100000
# arr = [i if i % 2 else arr_length - i for i in range(arr_length, 0, -1)]
arr = [random.randint(0, n * 100) for n in range(arr_length)]
# print("Original array:", arr)

# Perform multi-threaded quicksort
start_time = time.time()
quick_sort(arr, 0, len(arr) - 1)

# print("Sorted array:", arr)
print(f'Elapsed: {time.time() - start_time}')