def back(a):
    answer = ''
    if a == 0:
        return ''
    return answer + str(a % 10) + back(a // 10)
answer = back(int(input('Введите число, которое требуется перевернуть: ')))
print(f'Перевернутое число: {answer}')