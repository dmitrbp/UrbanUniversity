data = [5, 2, 3, 4, 1]
def bubble_sort(ls):
    for i in range(len(ls) - 1, 0, -1):
        for j in range(i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls

print(bubble_sort(data))