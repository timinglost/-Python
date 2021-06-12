from memory_profiler import memory_usage


def decor(func):
    def t(*args, **kwargs):
        m1 = memory_usage()
        func(*args, **kwargs)
        m2 = memory_usage()
        print(m2[0] - m1[0])
    return t


@decor
def nightmare(a):
    def even_odd(a):
        even = 0
        odd = 0
        if a == 0:
            return even, odd
        last = a % 10
        if (last % 2) == 0:
            even += 1
        else:
            odd += 1
        return even_odd(a // 10)[0] + even, even_odd(a // 10)[1] + odd
    return even_odd
nightmare(int(input('Введите число: ')))


@decor
def even_odd_cycle(n):
    even = 0
    odd = 0
    while n > 0:
        last = n % 10
        n //= 10
        if last % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'Количество четных и нечетных цифр в числе равно: ({even}, {odd})')


even_odd_cycle(1234567890)
"""
nightmare - 0.0078125 MiBs, even_odd_cycle - 0.0 MiBs. Цикл быстрее, ведь рекурсия
забивает память дополнительными вызовами функции.
"""
