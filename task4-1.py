from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [k for k, v in enumerate(nums) if v % 2 == 0]
    return new_arr


def func_2_1(nums):
    new_arr = [x for x in range(len(nums)) if nums[x] % 2 == 0]
    return new_arr


n = [x for x in range(1000)]
print('func_1:', timeit('func_1(n)', globals=globals(), number=1000))
print('func_2:', timeit('func_2(n)', globals=globals(), number=1000))
print('func_2_1:', timeit('func_2_1(n)', globals=globals(), number=1000))
"""
func_1 самый медленный из-за цикла и append.
func_2 чуть быстрее, благодаря отсутствию append.
func_2_1 самая быстрая, благодоря отсутствию append и enumerate.
PS.
func_1: 0.075282954
func_2: 0.06100090600000001
func_2_1: 0.05959048
"""