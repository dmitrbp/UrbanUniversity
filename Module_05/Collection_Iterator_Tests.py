col = [('One', 1), ('Two', 2)]
col1 = [y for x in col for y in x]
col2 = {x[0]:x[1] for x in col}
col3 = {x:y for (x, y) in col}

print(col)
print(col1)
print(col2)
print(col3)