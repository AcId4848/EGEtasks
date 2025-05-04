def f(c, e, s):
    if c > e:
        return 0
    if c == e:
        if s == 1:
            return 1
        else:
            return 0
    if c < e:
        if s == 0:
            return f(c + 1, e, s) + f(c + 2, e, s) + f(c * 2, e, s + 1)
        if s == 1:
            return f(c + 1, e, s) + f(c + 2, e, s)


print(f(2, 12, 0))