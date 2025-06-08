from fnmatch import fnmatch


def div(x):
    odd = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            if i % 2 == 1:
                odd.append(i)
            if x // i % 2 == 1:
                odd.append(x // i)
    return odd


for x in range(0, 10 ** 7, 217):
    d = div(x)
    if fnmatch(str(x), "14?4*") and x % 217 == 0:
        print(x, sum(d))

# 1484714 958464
# 1484931 2336768
# 1494045 3345408
# 1494262 964608
# 1494479 1806336
# 1494696 306432
# 1494913 1785088