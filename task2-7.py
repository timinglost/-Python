def equality(n):
    if n == 0:
        return 0, False
    else:
        return equality(n - 1)[0] + n, equality(n - 1)[0] + n == (n * (n + 1) / 2)
print(equality(int(input('Введите число: ')))[1])