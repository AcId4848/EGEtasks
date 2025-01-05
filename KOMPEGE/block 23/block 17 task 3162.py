def f(x, y, s):
    if x > y:
        return 0
    if x == y:
        return s == 1
    if x < y:
        return f(x + 1, y, s) + f(x + 2, y, s) + f(x * 2, y, s + 1)

print(f(2, 12, 0))