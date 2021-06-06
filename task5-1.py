from collections import namedtuple


def avg_profit():
    n = int(input('Введите количество предприятий для расчета прибыли: '))
    enterprises = namedtuple('enterprises', 'name q1 q2 q3 q4 quarterly_profit')
    firm_name = []
    avg_firm_profit = []
    for i in range(n):
        firm = str(input('Введите название предприятия: '))
        qu1, qu2, qu3, qu4 = str(input('через пробел введите прибыль данного предприятия\n'
                              'за каждый квартал(Всего 4 квартала): ')).split(' ')
        avg_quarterly_profit = (int(qu1) + int(qu2) + int(qu3) + int(qu4) / 4)
        obj = enterprises(firm, qu1, qu2, qu3, qu4, avg_quarterly_profit)
        firm_name.append(obj.name)
        avg_firm_profit.append(obj.quarterly_profit)
    avg_all = sum(avg_firm_profit) / n
    max_firm = ''
    min_firm = ''
    for i in firm_name:
        if avg_firm_profit[firm_name.index(i)] > avg_all:
            max_firm += f'{i} '
        else:
            min_firm += f'{i} '
    print(f'Средняя годовая прибыль всех предприятий: {avg_all}\n'
          f'Предприятия, с прибылью выше среднего значения: {max_firm}\n'
          f'Предприятия, с прибылью ниже среднего значения: {min_firm}')


avg_profit()
