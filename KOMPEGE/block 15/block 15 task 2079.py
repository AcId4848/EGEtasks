def f(x, A):
    return (x & 107 == 0) <= ((x & 55 != 0) <= (x & A != 0))


for A in range(1, 10000):
    if all(f(x, A) for x in range(10000)):
        print(A)
        break

# 20
