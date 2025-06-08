def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)


for x in range(800000, 1000000):
    d = div(x)
    if len(d) == 0:
        m = 0
    else:
        m = min(d) + max(d)
    if m % 10 == 4:
        print(x, m)
# 800004 400004
# 800009 114294
# 800013 266674
# 800024 400014
# 800033 61554