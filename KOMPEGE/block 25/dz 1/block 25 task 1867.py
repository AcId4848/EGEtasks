def div(x):
    minimal_18 = []
    c = 0
    for i in range(2, int(x ** 0.5) + 1):
        if i % 10 == 8 and x % i == 0 and i != 8:
            c += 1
            minimal_18.append(i)
        if x // i % 10 == 8 and x % (x // i) == 0 and x // i != 8:
            c += 1
            minimal_18.append(x // i)
    if c > 0:
        return minimal_18
    else:
        return 0

for x in range(500001, 500100):
    d = div(x)
    if d != 0:
        print(x, min(d))


# 500002 178
# 500004 18
# 500016 48
# 500018 58
# 500020 4348