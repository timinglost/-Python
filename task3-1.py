from time import time
from timeit import default_timer
def timesize(func):
    def t(*args, **kwargs):
        t_1 = time()
        func(*args, **kwargs)
        t_2 = time()
        print(t_2 - t_1)
    return t
# a
@timesize
def filling_list(a):
    i = 0
    while i < 10000000:
        a.append(i)
        i += 1
l = []
print('filling_list:')
filling_list(l)
@timesize
def filling_dict(a):
    i = 0
    while i < 10000000:
        a[f'key{i}'] = i
        i += 1
d = {}
print('filling_dict:')
filling_dict(d)
"""
Функция filling_list выполняется быстрее, потому что a[f'key{i}'] = i в filling_dict имеет f'key{i}', который усложняет операцию.
"""
# b
@timesize
def add_list(a, i, n):
    if i > (len(a) - 1):
        a.append(n)
    else:
        a.insert(i, n)
print('add_list:')
add_list(l, 100, 9)
@timesize
def add_dict(a, i, n):
    if a.get(i) is None:
        a[f'{i}'] = n
    else:
        print('Такой ключь уже существует')
print('add_dict:')
add_dict(d, 'key_test', 10)
"""
Функция add_dict быстрее, ведь имеет константную сложность, а add_list из-за a.insert(i, n) имеет линейную сложность.
"""
@timesize
def delete_list(a, i):
    if i > (len(a) - 1):
        a.pop()
    else:
        a.pop(i)
print('delete_list:')
delete_list(l, 100)
@timesize
def delete_dict(a, i):
    if a.get(i) is None:
        print('Такого ключа не существует')
    else:
        a.pop(i)
print('delete_dict:')
delete_dict(d, 'key99')
"""
Функции delete_list и delete_dict одинаковые, ведь имеют константную сложность.
"""
@timesize
def out_list(a, i):
    if i > (len(a) - 1):
        print('Такого индекса нет')
    else:
        print(a[i])
print('out_list:')
out_list(l, 100)
@timesize
def out_dict(a, i):
    if a.get(i) is None:
        print('Такого ключа не существует')
    else:
        print(f'{i}: {a[i]}')
print('out_dict:')
out_dict(d, 'key100')
"""
Функция out_list выполняется быстрее, потому что f'{i}: {a[i]}' в out_dict усложняет операцию.
"""
