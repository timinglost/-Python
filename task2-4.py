def sum_of_elements(n, num):
    return sum_of_elements(n - 1, (num / 2) * -1) + num if n > 0 else 0
print(sum_of_elements(3, 1))