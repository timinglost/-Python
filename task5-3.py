from collections import deque
from timeit import timeit


def lst_append(n):
    for i in range(n):
        lst.append(i)


def dq_append(n):
    for i in range(n):
        dq.append(i)


def lst_app_begin(n):
    for i in range(n):
        lst.insert(0, i)


def dq_app_begin(n):
    for i in range(n):
        dq.appendleft(i)


def lst_popleft(n):
    for i in range(n):
        lst.pop(0)


def dq_popleft(n):
    for i in range(n):
        dq.popleft()


def lst_extendleft(n):
    while n != 0:
        lst.insert(0, n)
        n -= 1


def dq_extendleft(n):
    dq.extendleft(range(n))


lst = []
dq = deque()
n = 1000
print('append')
print(f'lst_append:', timeit('lst_append(n)', globals=globals(), number=1000))
print(f'dq_append:', timeit('dq_append(n)', globals=globals(), number=1000))
print('app_begin')
print(f'lst_app_begin:', timeit('lst_app_begin(n)', globals=globals(), number=1))
print(f'dq_app_begin:', timeit('dq_app_begin(n)', globals=globals(), number=1))
print('popleft')
print(f'lst_popleft:', timeit('lst_popleft(n)', globals=globals(), number=1))
print(f'dq_popleft:', timeit('dq_popleft(n)', globals=globals(), number=1))
print('extendleft')
print(f'lst_extendleft:', timeit('lst_extendleft(n)', globals=globals(), number=1))
print(f'dq_extendleft:', timeit('dq_extendleft(n)', globals=globals(), number=1))
"""
deque работает быстрее list, во всех проверенных выше случаях.
PS.
append
lst_append: 0.110557793
dq_append: 0.06774112799999998 

app_begin
lst_app_begin: 0.682674218
dq_app_begin: 7.714299999994623e-05

popleft
lst_popleft: 0.4194491669999999
dq_popleft: 5.529100000001286e-05

extendleft
lst_extendleft: 0.524123235
dq_extendleft: 2.615599999988838e-05
"""
