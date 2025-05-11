from sys import setrecursionlimit

setrecursionlimit(10000)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n ** 2 + f(n - 1)


print(f(1000) - f(997))
# 2994005