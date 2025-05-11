from sys import setrecursionlimit

setrecursionlimit(100000)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (2 * n - 1) * f(n - 1)


print(f(3516)/f(3513))
# 347280657273