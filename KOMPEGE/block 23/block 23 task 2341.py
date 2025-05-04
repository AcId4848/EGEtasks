def f(c, e, count):
    if c > e or count > 8:
        return 0
    if c == e:
        if count == 8:
            return 1
        else:
            return 0
    if c < e:
        return f(c + 1, e, count + 1) + f(c + 5, e, count + 1) + f(c * 3, e, count + 1)


a = []
for i in range(1000, 1025):
    a.append(f(1, i, 0))

print(a)
# 1