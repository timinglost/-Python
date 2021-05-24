"""
Задание 6.
Задание на закрепление навыков работы с очередью
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""
class task_board:
    def __init__(self):
        self.basic = [] # базовая
        self.resolved = [] # решенная
        self.revision = [] # доработка

    def is_empty(self):
        return f'basic: {self.basic == []}, resolved: {self.resolved == []}, revision: {self.revision == []}'

    def to_queue(self, item):
        self.basic.insert(0, item)

    def b_to_res(self):
        last = (self.basic[len(self.basic) - 1])
        self.basic.pop()
        self.resolved.insert(0, last)

    def b_to_rev(self):
        last = (self.basic[len(self.basic) - 1])
        self.basic.pop()
        self.revision.insert(0, last)

    def rev_to_res(self):
        last = (self.revision[len(self.revision) - 1])
        self.revision.pop()
        self.resolved.insert(0, last)

    def size(self):
        return f'basic: {len(self.basic)}, resolved: {len(self.resolved)}, revision: {len(self.revision)}'
a = task_board()
print(a.is_empty())
i = 0
while i < 40:
    a.to_queue(f'zadacha {i}')
    i += 1
i = 0
while i < 15:
    a.b_to_res()
    i += 1
i = 0
while i < 5:
    a.b_to_rev()
    i += 1
i = 0
print(a.size())
while i < 5:
    a.rev_to_res()
    i += 1
print(a.size())
print(a.is_empty())
