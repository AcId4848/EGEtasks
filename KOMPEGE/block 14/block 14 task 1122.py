def f(x):
    s = ""
    while x != 0:
        s += str(x % 6)
        x //= 6
    return s[::-1]


def f1(x):
    return f(36 ** 17 - 6 ** x + 71)


for x in range(1000):
    if sum(int(c) for c in f1(x)) == 61:
        print(x)
        break

# 24