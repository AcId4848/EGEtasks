def f(c, e):
    if c > e:
        return 0
    if c == e:
        return 1
    if c < e:
        return f(c + 1, e) + f(c * 2, e)

print(f(1, 12) * f(12, 30))

# 100