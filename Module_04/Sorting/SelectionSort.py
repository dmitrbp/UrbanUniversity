# ==============================================================================
# Реализация алгоритма сортировки SELECTION (из практики, часть1) с ОШИБКОй !!!
# ==============================================================================
data1 = [5, 2, 3, 4, 1]
def selection_sort1(ls):
    for i in range(len(ls) - 1):
        min_index = i
        for j in range(i + 1, len(ls)):
            if ls[min_index] > ls[j]:
                min_index = j
                ls[min_index], ls[j] = ls[j], ls[min_index]
    return ls

print(selection_sort1(data1), '- Ошибка, список остался неотсортированным')

# ==============================================================================
# Реализация алгоритма сортировки SELECTION (из практики, часть1) с ИСПРАВЛЕННЫЙ
# ==============================================================================
data2 = [5, 2, 3, 4, 1]
def selection_sort2(ls):
    for i in range(len(ls) - 1):
        min_index = i
        for j in range(i + 1, len(ls)):
            # select the minimum element in every iteration
            if ls[j] < ls[min_index]:
                min_index = j
        ls[min_index], ls[i] = ls[i], ls[min_index]
    return ls

print(selection_sort2(data2), '- Правильно')
