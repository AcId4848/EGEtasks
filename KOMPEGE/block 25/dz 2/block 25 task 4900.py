from fnmatch import fnmatch

s = []

def div21(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sum(d) % 21


for x in range(10 ** 7, 0, -1):
    if fnmatch(str(x), "9?*55*7"):
        print(x, div21(x))
