"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""
# max_profit_1 - O(n)
def max_profit_1(s):
    k = list(s.keys()) # O(len(...))
    z = list(s.values()) # O(len(...))
    answer = {} # O(1)
    i = 0 # O(1)
    while i < 3: # O(log n)
        m = max(z) # O(n)
        ind = z.index(m)
        answer[f'{k[ind]}'] = z[ind] # O(1)
        k.pop(ind) # O(1)
        z.pop(ind) # O(1)
        i += 1 # O(1)
    return answer # O(1)
# max_profit_2 - O(n)
def max_profit_2(s):
    a = s # O(1)
    answer = {} # O(1)
    j = 0 # O(1)
    while j < 3: # O(log n)
        z = 0 # O(1)
        for i in a: # O(n)
            if a[i] > z: # O(1)
                k = i # O(1)
                z = a[i] # O(1)
        answer[f'{k}'] = z # O(1)
        a.pop(f'{k}') # O(1)
        j += 1 # O(1)
    return answer # O(1)
company = {'apple': 10000, 'google': 20000, 'htc': 5000, 'lg': 30000, 'huawei': 9999999}
print(max_profit_1(company))
print(max_profit_2(company))
"""
max_profit_2 является более эфективным решением задачи, ведь в нем только 1 O(n) и 1 O(log n), а в max_profit_1
1 O(n), 1 O(log n) и 2 O(len(...)). Следовательно max_profit_2 задействует меньше ресурсов компьютера и
является более производительным.
"""