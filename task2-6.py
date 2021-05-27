from random import randint
def game(num, counter):
    if counter == 0:
        return f'Вы проиграли, число {num}'
    answer = int(input(f'Осталось {counter} попыток\nВведите число: '))
    if answer > num:
        print('Число меньше')
        return game(num, counter - 1)
    if answer < num:
        print('Число больше')
        return game(num, counter - 1)
    if answer == num:
        return 'Вы выйграли!'
print(game(randint(1, 100), 10))