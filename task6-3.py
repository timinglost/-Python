from memory_profiler import memory_usage


def decor(func):
    def t(*args, **kwargs):
        m1 = memory_usage()
        func(*args, **kwargs)
        m2 = memory_usage()
        print(m2[0] - m1[0])
    return t


@decor
def one():
    def two():
        lst = []
        for i in range(1000000):
            lst.append(i)


one()
"""
Чтобы замерить рекурсию, нужно поместить ее в другую функцию, иначе декоратор посчитает 
каждый шаг рекурсии по отдельности. Я это понял когда в task6-1-s-1, когда я еще не 
решил замерять через свой деоратор, попытался помереть рекурию @profile-ом и на каждый шаг
рекурсии он делал отдельную таблицу.
"""
