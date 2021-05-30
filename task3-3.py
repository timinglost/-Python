def unique_substrings(n):
    long = len(n) - 1
    a = []
    while long > 0:
        i = 0
        while i < len(n):
            a.append(f'{n[i:(i + long)]}')
            i += 1
        long -= 1
    b = set()
    for i in a:
        b.add(hash(i))
    answer = []
    for i in b:
        for j in a:
            if hash(j) == i:
                answer.append(j)
                break
    print(f'{n} - {len(answer)} уникальных подстрок')
    for i in answer:
        print(i)
unique_substrings('рара')
