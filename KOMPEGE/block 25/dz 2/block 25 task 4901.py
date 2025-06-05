from fnmatch import fnmatch


def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {x, x // i}
    return d


for x in range(1000, 1000000000):
    d = div(x)
    if fnmatch(str(x), "?6*6*?6") and 7 in d and 6 in d and 8 in d:
        print(x, sum(d))
