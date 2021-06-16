import timeit
import random
import operator


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


lst = [random.uniform(0, 50) for _ in range(10)]
lst_one = [random.uniform(0, 50) for _ in range(100)]
lst_tow = [random.uniform(0, 50) for _ in range(1000)]
lst_tree = [random.uniform(0, 50) for _ in range(10000)]
# lst_four = [random.uniform(0, 50) for _ in range(100000)]
print(lst)
print(merge_sort(lst))
print('merge_sort(lst[:]):',
      timeit.timeit("merge_sort(lst[:])", globals=globals(), number=1000))
print('merge_sort(lst_one[:]):',
      timeit.timeit("merge_sort(lst_one[:])", globals=globals(), number=1000))
print('merge_sort(lst_tow[:]):',
      timeit.timeit("merge_sort(lst_tow[:])", globals=globals(), number=1000))
print('merge_sort(lst_tree[:]):',
      timeit.timeit("merge_sort(lst_tree[:])", globals=globals(), number=1000))
# print('merge_sort(lst_four[:]):',
#       timeit.timeit("merge_sort(lst_four[:])", globals=globals(), number=1000))
"""
Исходный массив:
    [20.59435113799801, 33.01693370731133, 10.404699492145664, 7.1423863928949896, 
    13.722314613355952, 8.553578270739964, 46.1735656523958, 21.805618421447004, 
    30.181759931733726, 37.72682496701086]
Отсортированный массив:
    [7.1423863928949896, 8.553578270739964, 10.404699492145664, 13.722314613355952, 
    20.59435113799801, 21.805618421447004, 30.181759931733726, 33.01693370731133,
    37.72682496701086, 46.1735656523958]
Замеры:
(10)       merge_sort(lst[:]):         0.013197760000000003
(100)      merge_sort(lst_one[:]):     0.21026824300000002
(1000)     merge_sort(lst_tow[:]):     2.742496675
(10000)    merge_sort(lst_tree[:]):    37.402929319
(100000)   бесконечность
PS.
Решение не было придумано, оно было найдено.
"""
