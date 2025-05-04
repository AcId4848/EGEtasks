def f(c, e):
    if c > e:
        return 0
    if c == e:
        return 1
    if c < e:
        return f(c + 2, e) + f(c + 4, e) + f(c + 5, e)

for N in range(1000):
    if f(31, N) == 1001:
        print(N)
        break

# 56