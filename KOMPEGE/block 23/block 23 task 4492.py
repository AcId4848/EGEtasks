def f(c, e, s):
    if c % 2 != 0:
        s += 1
    if c > e or s > 1:
        return 0
    if c == e:
        if s == 1:
            return 1
        else:
            return 0
    if c < e:
        return f(c + 1, e, s) + f(c + 2, e, s) + f(c * 2, e, s)


print(f(2, 40, 0))
# 626