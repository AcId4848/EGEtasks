from sys import setrecursionlimit

setrecursionlimit(100000)


def f(n):
    if n > 100000:
        return n
    if n <= 100000:
        return f(n + 1) + 5 * n + 2


print(f(3) - f(7))
# 98