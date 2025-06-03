def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0 and i % 2 == 0:
            d |= {i}
        if x % i == 0 and (x // i) % 2 == 0:
            d |= {x // i}
    return sorted(d)


for x in range(1204300, 1204380 + 1):
    d = div(x)
    if len(d) != 0:
        s = sum(d)
    else:
        s = 0
    if s != 0 and s % 10 == 0:
        print(x, s)


