def f(c, e, s):
    if c > e:
        return 0
    if c == e:
        return 1
    if c < e:
        if s % 2 == 0:
            return f(c + 1, e, s) + f(c + 2, e, s) + f(c * 2, e, s + 1)
        else:
            return f(c + 1, e, s + 1) + f(c + 2, e, s + 1)


print(f(1, 15, 0))
# 1545