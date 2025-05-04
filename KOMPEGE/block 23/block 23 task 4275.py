def f(c, e, s):
    if c > e or s > 3:
        return 0
    if c == e:
        return 1
    if c < e:
        if s < 3:
            return f(c + 2, e, s) + f(c * 3, e, s + 1) + f(c * 5, e, s + 1)
        else:
            return f(c + 2, e, s)

print(f(2, 200, 0))

# 793