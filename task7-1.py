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
n = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]
print(orig_list)
print(bubble_sort_waning(orig_list[:]))
print(bubble_sort_waning(n[:]))
print('bubble_sort(orig_list[:]):',
      timeit.timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
print('bubble_sort_waning(orig_list[:]):',
      timeit.timeit("bubble_sort_waning(orig_list[:])", globals=globals(), number=1000))
print('bubble_sort_waning(n[:]):',
      timeit.timeit("bubble_sort_waning(n[:])", globals=globals(), number=1000))
"""
bubble_sort медленный, ведь на каждом шаге цикла while в for перебирается
весь массив. bubble_sort_waning быстрее, ведь на каждом шаге цикла while в for 
не перебирается весь массив, а только не отсортированная часть.
check = False/True ускоряет работу только в редких случаях,
когда массив уже отсортирован. Доработка помогла.
Замеры:
    bubble_sort(orig_list[:]):        0.010102104
    bubble_sort_waning(orig_list[:]): 0.007815953
    bubble_sort_waning(n[:]):         0.0009627990000000003
"""
