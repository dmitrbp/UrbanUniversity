import inspect
class A():
    c_attr0: str = 'c0'
    c_attr: str
    # i_attr: str
    def __init__(self, i_attr):
        self.i_attr: str = i_attr


a1 = A('i1')
a1.c_attr = 'c1'
a1.c_attr0 = 'c00'

a2 = A('i2')
a2.c_attr = 'c2'

A.c_attr0 = 'c01'

print(a1.c_attr, a1.i_attr, a2.c_attr, a2.i_attr, A.c_attr0, a1.c_attr0, a2.c_attr0)
print(vars(a1))
for name, value in inspect.getmembers(a1):
    if not name.startswith('__'):
        print(f"{name}: {value}")
