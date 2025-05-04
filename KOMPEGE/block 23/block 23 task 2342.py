def f(c, e):
    if c > e:
        return 0
    if c == e:
        return 1
    if c < e:
        return f(c + 1, e) + f([c + 10, c + 11][1 if c % 10 != 9 else 0], e)

print(f(25, 51))
# 33