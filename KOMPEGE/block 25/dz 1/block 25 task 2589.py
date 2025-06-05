def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0 and i % 3 == 0:
            d |= {i}
        if x % i == 0 and x // i % 3 == 0:
            d |= {x // i}
    return sorted(d)

for x in range(300000, 300500):
    d = div(x)
    if len(d) == 5:
        print(x, d[-1])

# 300051 100017
# 300075 60015
# 300156 150078
# 300159 100053