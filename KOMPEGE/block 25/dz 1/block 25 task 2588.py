def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0 and i % 2 == 0:
            d |= {i}
        if x % i == 0 and (x // i) % 2 == 0:
            d |= {x // i}
    return sorted(d)


for x in range(190201, 190260 + 1):
    d = div(x)
    if len(d) == 4:
        print(d[3], d[2])

# 190226 838
# 190234 17294
# 190238 2606
# 190252 95126
# 190258 758