import math


def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)


for x in range(400000000, 600000000):
    d = div(x)
    if len(d) < 5:
        pn = 0
    else:
        pn = math.prod(d[:5])
    if pn % 100 == 17 and pn <= x:
        print(pn, d[4])

# 782217 37
# 166617 33
# 2880117 93
# 74874717 111
# 725517 53