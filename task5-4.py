from collections import OrderedDict
from timeit import timeit


def dict_add(n):
    for i in range(n):
        d[i] = i


def OD_add(n):
    return OrderedDict(n)


def watch_dict(n):
    for i in range(n):
        a = d[i]


def watch_OD(n):
    for i in range(n):
        a = OD[i]


d = {}
n = 1000
dict_add(n)
OD = OD_add(d)
watch_dict(n)
print(f'dict_add:', timeit('dict_add(n)', globals=globals(), number=1000))
print(f'OD_add:', timeit('OD_add(d)', globals=globals(), number=1000))
print(f'watch_dict:', timeit('watch_dict(n)', globals=globals(), number=1000))
print(f'watch_OD:', timeit('watch_OD(n)', globals=globals(), number=1000))
"""
OrderedDict и обычный словарь (+-) одинаковы по скорости. Не имеет смысла использовать OrderedDict
в новых версиях Python.
"""
