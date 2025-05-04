def f(x, A):
    return ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & A != 0))


for A in range(1, 1000):
    if all(f(x, A) for x in range(10000)):
        print(A)
        break

# 2