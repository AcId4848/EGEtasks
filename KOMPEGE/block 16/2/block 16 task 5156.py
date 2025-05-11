from sys import setrecursionlimit

setrecursionlimit(100000)


def f(n):
    if n <= 3:
        return n
    if n > 3 and n % 2 != 0:
        return 2 * n + f(n - 2)
    if n > 3 and n % 2 == 0:
        return n ** 2 + f(n - 1)


print(f(10000) - f(9995))