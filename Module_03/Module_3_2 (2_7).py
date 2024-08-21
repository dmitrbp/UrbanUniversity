def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# 1
print_params()
print_params(2, 'строка1', False)
print_params(b = 25)
print_params(c = [1, 2, 3])
# 2
values_list = [100, 'строка2', True]
values_dict = {"a" : 5, "b" : 'строка3', "c" : True}
print_params(*values_list)
print_params(**values_dict)
# 3
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
