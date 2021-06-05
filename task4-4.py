from timeit import timeit
from collections import Counter
array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    max_2 = max(map(array.count, array))
    elem = max(a for a in array if array.count(a) == max_2)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3_1():
    max_2 = max(array, key=array.count)
    elem = array.count(max_2)
    return f'Чаще всего встречается число {max_2}, ' \
           f'оно появилось в массиве {elem} раз(а)'


def func_3_2():
    lst = Counter(array)
    elem = max(list(lst.items()), key=lambda x: x[1])
    return f'Чаще всего встречается число {elem[0]}, ' \
           f'оно появилось в массиве {elem[1]} раз(а)'


print('func_1:', timeit('func_1', globals=globals(), number=10000000))
print('func_2:', timeit('func_2', globals=globals(), number=10000000))
print('func_3:', timeit('func_3', globals=globals(), number=10000000))
print('func_3_1:', timeit('func_3_1', globals=globals(), number=10000000))
print('func_3_2:', timeit('func_3_2', globals=globals(), number=10000000))
"""
У меня не получилось сделать более быструю функцию.
Все функции выполняются с (+-) одинаковой скоростью.
PS.
1 try:
    func_1: 0.169205709
    func_2: 0.16692519
    func_3: 0.169039504
    func_3_1: 0.166545434
    func_3_2: 0.19798236299999994
2 try:
    func_1: 0.169615262
    func_2: 0.16812835499999998
    func_3: 0.16879549299999996
    func_3_1: 0.16659079300000001
    func_3_2: 0.1686534580000001
3 try:
    func_1: 0.181383376
    func_2: 0.18173598199999996
    func_3: 0.16865378799999997
    func_3_1: 0.16846142799999997
    func_3_2: 0.167459562
"""
