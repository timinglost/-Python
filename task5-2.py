from collections import defaultdict
from functools import reduce


def multiplication(x, z):
    return x * z


def operation_number(a, b):
    meaning = defaultdict(list)
    meaning[a] = list(a)
    meaning[b] = list(b)
    c = hex(sum([int(''.join(x), 16) for x in meaning.values()])).split('x')[1].upper()
    d = hex(reduce(multiplication, [int(''.join(num), 16) for num in meaning.values()])).split('x')[1].upper()
    meaning['summ'] = list(c)
    meaning['mul-on'] = list(d)
    print(f'Сумма чисел из примера: {meaning["summ"]}\n'
          f'Произведение - {meaning["mul-on"]}')


operation_number('A2', 'C4F')
