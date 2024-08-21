first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) - len(y) != 0)
# second_result = (len(first[i]) == len(second[j]) for i in range(len(first)) for j in range(len(second)) if i == j)
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))
