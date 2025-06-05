def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)


for x in range(500000, 0, -1):
    d = div(x)
    d1 = []
    for j in d:
        if len(div(j)) == 2:
            d1.append(j)
    s = sum(d1)
    if s != 0 and s % 10 == 0:
        print(x, s)


# 499996 2560
# 499995 320
# 499994 22740
# 499989 860
# 499981 13550
# 499971 166660
# 499959 18520