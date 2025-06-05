def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)


for x in range(125697, 125721+1):
    d = div(x)
    d1 = []
    for j in d:
        if len(div(j)) == 2:
            d1.append(j)
    if len(d1) == 2 and d1[0] * d1[1] == x:
        print(*d1)
# 7 17957
# 337 373
# 2 62851
# 3 41903
# 7 17959