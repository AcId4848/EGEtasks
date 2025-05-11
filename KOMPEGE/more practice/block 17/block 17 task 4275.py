def f(x, y, s):
    if x > y:
        return 0
    if x == y:
        return s <= 3
    if x < y:
        return f(x + 2, y, s) + f(x * 3, y, s+1) + f(x * 5, y, s + 1)

print(f(2, 200, 0))