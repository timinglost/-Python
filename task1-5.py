"""
Задание 5.
Задание на закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.
После реализации структуры, проверьте ее работу на различных сценариях
Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""
class stack_of_plates:
    def __init__(self):
        self.elems = [[]]
        self.chek = 1
        self.ind = 0

    def is_empty(self):
        return self.elems[self.ind] == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if self.chek > 5:
            self.elems.append([])
            self.ind += 1
            self.chek = 1
        self.elems[self.ind].append(el)
        self.chek += 1
        print(self.elems)

    def pop_out(self):
        last = self.get_val()
        self.elems[self.ind].pop()
        if self.chek == 2:
            self.elems.pop()
            self.chek = 6
            if self.ind == 0:
                pass
            else:
                self.ind -= 1
        else:
            self.chek -= 1
        print(f'delete {last}')

    def get_val(self):
        return self.elems[self.ind][len(self.elems[self.ind]) - 1]

    def stack_size(self):
        num = 0
        for i in self.elems:
            num += (len(i))
        return f'{num} тарелок, {len(self.elems)} стопок'
a = stack_of_plates()
print(a.is_empty())
i = 0
while i < 23:
    a.push_in(f'тарелка{i}')
    i += 1
print(a.is_empty())
print(a.get_val())
a.pop_out()
i = 0
while i < 5:
    a.pop_out()
    i += 1
print(a.get_val())
print(a.stack_size())
