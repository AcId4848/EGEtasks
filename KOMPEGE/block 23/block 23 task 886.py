import sys

sys.setrecursionlimit(1000000000)


def f(c, e, count):
    if c > e or count > 7:
        return 0
    if c == e:
        if count == 7:
            return 1
        else:
            return 0
    if c < e:
        return f(c + 1, e, count + 1) + f(c + 4, e, count + 1) + f(c * 2, e, count + 1)


print(f(3, 27, 0))
# 37