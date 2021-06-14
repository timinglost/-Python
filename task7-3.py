import random
import timeit


def median_gnome(lst, m):
    i, size = 1, len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    return lst[m]


def median_max(lst):
    long = (len(lst) // 2) + 1
    while len(lst) > long:
        lst.pop(lst.index(max(lst)))
    return max(lst)


def median_left_right(lst):
    left, right = [], []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] > lst[j]:
                left.append(lst[j])
            if lst[i] < lst[j]:
                right.append(lst[j])
            if lst[i] == lst[j] and i > j:
                left.append(lst[j])
            if lst[i] == lst[j] and i < j:
                right.append(lst[j])
        if len(left) == len(right):
            return lst[i]
        left.clear()
        right.clear()


m = 4
lst = [random.randint(-100, 100) for _ in range((2 * m) + 1)]
print(median_gnome(lst[:], m))
print(median_max(lst[:]))
print(median_left_right(lst[:]))
print('median_gnome(lst, m):',
      timeit.timeit("median_gnome(lst[:], m)", globals=globals(), number=1000))
print('median_max(lst):',
      timeit.timeit("median_max(lst[:])", globals=globals(), number=1000))
print('median_left_right(lst):',
      timeit.timeit("median_left_right(lst[:])", globals=globals(), number=1000))
"""
Скорость median_gnome нормальная, имеет сложность O(n**2).
median_max самая быстрая, ведь в ней используются встроенные функции.
median_left_right самая медленная, ведь у неё цикл в цикле.
Замеры:
    median_gnome(lst, m):   0.007334554
    median_max(lst):        0.0018802389999999988
    median_left_right(lst): 0.014684999000000004
"""
