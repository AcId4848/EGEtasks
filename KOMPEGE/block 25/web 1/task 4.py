def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for x in range(244143, 367821):
    d = div(x)
    if len(d) == 5:
        print(d)