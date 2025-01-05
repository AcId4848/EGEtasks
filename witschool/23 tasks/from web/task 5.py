def f(x, y):
    if x > y or x == 44:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 2, y) + f(x * 3, y)

print(f(2, 24) * f(24, 144))