import hashlib
password = str(input('Введите пароль: '))
a = hashlib.sha256(password.encode('utf-8'))
b = a.hexdigest()
print(f'В базе данных хранится строка: {b}')
text = open('password.txt', 'w+')
text.write(f'{b}')
check_password = str(input('Введите пароль еще раз для проверки: '))
c = hashlib.sha256(check_password.encode('utf-8'))
d = c.hexdigest()
text = open('password.txt')
if d == text.read():
    print('Вы ввели правильный пароль')
else:
    print('Вы ввели не правильный пароль')
text.close()
