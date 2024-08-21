def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()         # выполняется корректно
# inner_function()      # ошибка компиляции: NameError: name 'inner_function' is not defined
