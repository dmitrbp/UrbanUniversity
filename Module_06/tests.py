class Employee:
    # конструктор с одним параметром
    def __init__(self, name):
        self.name = name

    # конструктор с двумя параметрами
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

# ira = Employee('Ира') - Ошибка
masha = Employee('Маша', 'Климентьева')

class A:
    def __init__(self, a):
        self.a = a

class B:
    def __init__(self, b):
        self.b = b

class C(A, B):
    def __init__(self, a, b, c):
        # Явный вызов конструктора класса A
        A.__init__(self, a)
        # Явный вызов конструктора класса B
        B.__init__(self, b)
        self.c = c

c = C(a=1, b=2, c=3)
print(c.a)  # 1
print(c.b)  # 2
print(c.c)  # 3

