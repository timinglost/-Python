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
e, o = even_odd(int(input('Введите число: ')))
print(f'Количество четных и нечетных цифр в числе равно: ({e}, {o})')