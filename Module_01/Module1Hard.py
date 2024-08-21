grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# variant 1
grades_mid1 = list(map(lambda n1, n2: n1 / n2, list(map(sum, grades)), list(map(len, grades))))
dict1 = dict(zip(sorted(list(students)), grades_mid1))
print(dict1)
# variant 2
grades_mid2 = [sum(g)/len(g) for g in grades]
dict2 = dict(zip(sorted(students), grades_mid2))
print(dict2)

