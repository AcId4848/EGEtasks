def f(x, y, s):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        if s % 2 == 0:
            return f(x + 1, y, s) + f(x + 2, y, s) + f(x * 2, y, s+1)
        else:
            return f(x + 1, y, s+1) + f(x + 2, y, s+1)

print(f(1, 15, 0))