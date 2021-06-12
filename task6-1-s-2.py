from memory_profiler import memory_usage


def decor(func):
    def t(*args, **kwargs):
        m1 = memory_usage()
        func(*args, **kwargs)
        m2 = memory_usage()
        print(m2[0] - m1[0])
    return t


class ComplexDigit:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return f'Комплексное сложение = {self.a + other.a} + {self.b + other.b}*i'
    def __mul__(self, other):
        return f'Комплексное умнажение = {(self.a * other.a) - (self.b * other.b)} + {(self.a * other.b) + (other.a * self.b)}*i'


@decor
def test():
    x = ComplexDigit(10, 3)
    y = ComplexDigit(8, 7)
    print(x + y)
    print(x * y)


class ComplexDigitOne:
    __slots__ = ['a', 'b']

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Комплексное сложение = {self.a + other.a} + {self.b + other.b}*i'

    def __mul__(self, other):
        return f'Комплексное умнажение = {(self.a * other.a) - (self.b * other.b)} + {(self.a * other.b) + (other.a * self.b)}*i'


@decor
def test1():
    x = ComplexDigitOne(10, 3)
    y = ComplexDigitOne(8, 7)
    print(x + y)
    print(x * y)


test()
test1()
"""
ComplexDigit - 0.0078125 MiBs, ComplexDigitOne - 0.0 MiBs. Потребление памяти снизилось, благодаря __slots__, котрый
оборачивает значения не в словарь, который много весит, а в список(в данном случае).
"""
