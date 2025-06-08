from fnmatch import fnmatch


def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return d


for x in range(1000, 1000000000):
    d = div(x)
    if fnmatch(str(x), "?6*6*?6") and 7 in d and 6 in d and 8 in d:
        print(x, sum(d))


# 56616 162240
# 66696 191040
# 161616 527744
# 166656 523264
# 266616 862680
# 360696 1094400
# 366576 1083264