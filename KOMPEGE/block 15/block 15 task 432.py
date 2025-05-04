def f(x, A):
    return (x % 84 != 0 or x % 90 != 0) <= (x % A != 0)


for A in range(1, 10000):
    if all(f(x, A) for x in range(10000)):
        print(A)
        break
# 1260