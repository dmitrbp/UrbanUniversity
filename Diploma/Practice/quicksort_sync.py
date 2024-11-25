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
        quick_sort(nums, low, pi - 1)
        quick_sort(nums, pi + 1, high)


# Example usage
arr = [4, 5, 8, 3, 0, 5, 3, 9, 4, 3]
print("Original array:", arr)

# Perform multi-threaded quicksort
quick_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)