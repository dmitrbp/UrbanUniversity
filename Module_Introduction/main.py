# 1st program
print(9 ** 0.5 * 5)

# 2nd program
print( True if 9.99 > 9.98 and 1000 != 1000.1 else False )

# 3rd program
result1 = 2 * 2 + 2
result2 = 2 * (2 + 2)
print(result1)
print(result2)
print(result1 == result2)

# 4th program
string = '123.456'
# First variant
for index in range(len(string)):
    if string[index] == '.':
        print(string[index+1])
        break
# Second variant
print(int(float(string) * 10) % 10)
