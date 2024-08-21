def apply_all_func(int_list, *functions):
    # Variant 1
    # ---------
    # result = {}
    # for function in functions:
    #     result[function.__name__] = function(int_list)
    # return result

    # Variant 2
    # ---------
    return {function.__name__: function(int_list) for function in functions}


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
