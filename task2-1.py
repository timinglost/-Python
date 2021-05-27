
def calculator():
    operations = ['0', '+', '-', '*', '/']
    o = str(input('Введите операцию (+, -, *, / или 0 для выхода): '))
    if o not in operations:
        print('Такой операции нет')
        return calculator()
    if o == '0':
        return
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
    except ValueError:
        print('Вы вместо трехзначного числа ввели строку (((. Исправьтесь')
        return calculator()
    if b == 0 and o == '/':
        print('На ноль делить нельзя')
        return calculator()
    if o == '+':
        answer = a + b
        print(f'Ваш результат {answer}')
        return calculator()
    if o == '-':
        answer = a - b
        print(f'Ваш результат {answer}')
        return calculator()
    if o == '*':
        answer = a * b
        print(f'Ваш результат {answer}')
        return calculator()
    if o == '/':
        answer = a / b
        print(f'Ваш результат {answer}')
        return calculator()
calculator()