from fnmatch import fnmatch

s = []

def div21(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sum(d) % 21


for x in range(0, 10 ** 7):
    if fnmatch(str(x), "9?*55*7"):
        print(x, div21(x))

# 9995597 18
# 9996557 12
# 9997557 12
# 9998557 17
# 9999557 0