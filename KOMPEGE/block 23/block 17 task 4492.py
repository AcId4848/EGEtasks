def f(x, y, k):
    if x % 2 != 0:
        k += 1
    if x > y or k > 1:
        return 0
    if x == y:
        return k == 1
    if x < y:
        return f(x + 1, y, k) + f(x + 2, y, k) + f(x * 2, y, k)


print(f(2, 40, 0))