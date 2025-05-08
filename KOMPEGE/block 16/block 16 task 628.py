from functools import lru_cache

@lru_cache(None)


def f(n):
    if n <= 18:
        return n + 3
    if n > 18 and n % 3 == 0:
        return (n // 3) * f(n // 3) + n - 12
    if n > 18 and n % 3 != 0:
        return f(n - 1) + n ** 2 + 5

array = []
for i in range(1, 1001):
    if len(str(f(i))) == len([i for i in str(f(i)) if int(i) % 2 == 0]):
        array.append(f(i))

print(len(array))
# 16