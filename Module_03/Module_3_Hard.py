def calculate_structure_sum(dt_structure, res=0):
    # if type(dt_structure) in (list, tuple, set):
    if isinstance(dt_structure, (list, tuple, set)):
        for item in dt_structure:
            res = calculate_structure_sum(item, res)
    elif isinstance(dt_structure, dict):
        for item in dt_structure.items():
            res = calculate_structure_sum(item, res)
    elif isinstance(dt_structure, int):
        res += dt_structure
    # elif type(dt_structure) is str:
    elif isinstance(dt_structure, str):
        res += len(dt_structure)
    return res


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
