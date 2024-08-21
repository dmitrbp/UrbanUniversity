class Test:
    gv = 'gstr'
    gc = []
    def __init__(self):
        self.lv = 'lstr'
        self.gv = 'gstr-i'
        self.gc.append('app')

    def instance_method(self):
        print(self.gv, self)
    @classmethod
    def class_method(cls):
        print(cls.gv, cls)
    @staticmethod
    def static_method():
        print(Test.gv, 'Static has no access to instance')

t1 = Test()
t2 = Test()
print(Test.gv, t1.gv, t2.gv)

t1.gv = 'gstr1'
t2.gv = 'gstr2'
t1.lv = 'lstr1'
t2.lv = 'lstr2'

print(Test.gv, t1.gv, t2.gv, t1.lv, t2.lv, t1.gc, t2.gc)
print(t1.gv is Test.gv)
print(t1.gc is t2.gc)
t1.class_method()
t1.instance_method()
t2.class_method()
t2.instance_method()
t1.static_method()