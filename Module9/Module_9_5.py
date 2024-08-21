class StepValueError(ValueError):
    def __init__(self, message):
        self.message = message

class Iterator:
    def __init__(self, start, stop, step=1):
        if not step:
            raise StepValueError('Шаг указан неверно')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = self.start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.pointer if self.step > 0 else self.stop) > (self.stop if self.step > 0 else self.pointer):
            raise StopIteration()
        pointer_for_return = self.pointer
        self.pointer += self.step
        return pointer_for_return

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as e:
    print(e.message)

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
