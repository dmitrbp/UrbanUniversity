immutable_var = (1, 1.2, "Строка", False)
print(immutable_var)
# immutable_var[0] = 2 - изменения элементов кортежа запрещены
mutable_list = [2, 2.3, "String element", True]
mutable_list[0] = 3
mutable_list[1] = 3.3
mutable_list[2] = "String element replaced"
mutable_list[3] = False
print(mutable_list)
