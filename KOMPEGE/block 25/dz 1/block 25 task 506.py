def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for x in range(25317, 51237 + 1):
    d = div(x)
    s = []
    for j in d:
        if len(div(j)) == 2:
            s.append(j)
    if len(s) >= 6:
        print(x, max(s))
