def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        is_simple = True
        for i in range(2, int(res ** 0.5) + 1):
            if res % i == 0:
                is_simple = False
                break
        if is_simple:
            print('Простое')
        else:
            print('Составное')
        return res
    return wrapper

@is_prime
def sum_three(one, two, three):
    return one + two + three


result = sum_three(2, 3, 6)
print(result)