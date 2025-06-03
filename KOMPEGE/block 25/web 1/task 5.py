def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)


for x in range(135790, 163228+1):
    d = div(x)
    if sum(d) > 460000:
        print(len(d), sum(d))