from timeit import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    answer = ''
    while enter_num != 0:
        num = enter_num % 10
        answer = answer + f'{num}'
        enter_num //= 10
    return answer


n = 1234567890

print('revers_1:')
print(timeit('revers_1(n)', globals=globals(), number=1000))
run('revers_1(n)')

print('revers_2:')
print(timeit('revers_2(n)', globals=globals(), number=1000))
run('revers_2(n)')

print('revers_3:')
print(timeit('revers_3(n)', globals=globals(), number=1000))
run('revers_3(n)')

print('revers_4:')
print(timeit('revers_4(n)', globals=globals(), number=1000))
run('revers_4(n)')
"""
revers_1 самя медленная, ведь в ней рекурсия и в ней происходит n + 3 function calls(в данном
случае 14), когда в остальных функциях 4.
revers_2 и revers_4 одинаковые по скорости(+-), ведь в них
выполняется цикл перебирающий каждую цифру по отдельности. 
revers_3 самя быстрая, ведь 
выполняет только 2 простых действия.
"""
