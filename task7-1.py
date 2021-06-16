import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_waning(lst_obj):
    n = 1
    check = False
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                check = True
        if check is False:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
orig_list_one = [random.randint(-1000, 1000) for _ in range(100)]
orig_list_two = [random.randint(-10000, 10000) for _ in range(1000)]
orig_list_tree = [random.randint(-100000, 100000) for _ in range(10000)]
n = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]
print(orig_list)
print(bubble_sort_waning(orig_list[:]))
print(bubble_sort_waning(n[:]))
print('(10):')
print('bubble_sort(orig_list[:]):',
      timeit.timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
print('bubble_sort_waning(orig_list[:]):',
      timeit.timeit("bubble_sort_waning(orig_list[:])", globals=globals(), number=1000))
print('(100):')
print('bubble_sort(orig_list_one[:]):',
      timeit.timeit("bubble_sort(orig_list_one[:])", globals=globals(), number=1000))
print('bubble_sort_waning(orig_list_one[:]):',
      timeit.timeit("bubble_sort_waning(orig_list_one[:])", globals=globals(), number=1000))
print('(1000):')
print('bubble_sort(orig_list_two[:]):',
      timeit.timeit("bubble_sort(orig_list_two[:])", globals=globals(), number=1000))
print('bubble_sort_waning(orig_list_two[:]):',
      timeit.timeit("bubble_sort_waning(orig_list_two[:])", globals=globals(), number=1000))
print('(10000):')
print('bubble_sort(orig_list_tree[:]):',
      timeit.timeit("bubble_sort(orig_list_tree[:])", globals=globals(), number=1000))
print('bubble_sort_waning(orig_list_tree[:]):',
      timeit.timeit("bubble_sort_waning(orig_list_tree[:])", globals=globals(), number=1000))
print('n:')
print('bubble_sort_waning(n[:]):',
      timeit.timeit("bubble_sort_waning(n[:])", globals=globals(), number=1000))
"""
bubble_sort медленный, ведь на каждом шаге цикла while в for перебирается
весь массив. bubble_sort_waning быстрее, ведь на каждом шаге цикла while в for 
не перебирается весь массив, а только не отсортированная часть.
check = False/True ускоряет работу только в редких случаях,
когда массив уже отсортирован. Доработка 'check' не помогла.
Замеры:
    (10):
        bubble_sort(orig_list[:]):                  0.010937746999999998
        bubble_sort_waning(orig_list[:]):           0.00899295
    (100):
        bubble_sort(orig_list_one[:]):              0.878210786
        bubble_sort_waning(orig_list_one[:]):       0.600793414
    (1000):
        bubble_sort(orig_list_two[:]):              100.604257564
        bubble_sort_waning(orig_list_two[:]):       64.473418122
    (10000):
        Бесконечность
PS.
Извиняюсь. Я в предыдущем варианте решения, просто коряво изъяснился.
Я сравнивал bubble_sort с bubble_sort_waning и написал что доработка помогла,
имея в виду «for i in range(len(lst_obj) - 1):» -> «for i in range(len(lst_obj)-n):».
"""
