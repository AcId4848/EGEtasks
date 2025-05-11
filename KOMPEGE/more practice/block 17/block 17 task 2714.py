def f(x, y, k):
    if x % 2 == 0:
        k += 1
    if x > y or k > 6:
        return 0
    if x == y:
        return k == 6
    if x < y:
        return f(x + 1, y, k) + f(x + 3, y, k) + f(x + 5, y, k)


print(f(3, 25, 0))