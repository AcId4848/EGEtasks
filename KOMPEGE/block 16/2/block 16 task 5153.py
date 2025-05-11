from sys import setrecursionlimit

setrecursionlimit(100000)

def f(n):
    if n < 4:
        return 1
    if n > 3 and n % 2 != 0:
        return n
    if n > 3 and n % 2 == 0:
        return f(n - 1) + f(n - 2) + f(n - 3)


print(f(2254) - f(2252))
# 4504
