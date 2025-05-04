def f(x, A):
    return (x % A == 0 and x % 24 == 0 and x % 16 != 0) <= (x % A != 0)


for A in range(1, 1000):
    if all(f(x, A) for x in range(10000)):
        print(A)
        break
# 16