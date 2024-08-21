for number in list(range(3, 21)):
    password = ""
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                password += f"{i}{j}"
    print(f"{number} - {password}")
