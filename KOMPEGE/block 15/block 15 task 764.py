def f(x, A):
    return (x % 15 == 0 and x % 21 != 0) <= (x % A != 0 or x % 15 != 0)

for A in range(1, 1000):
    if all(f(x, A) for x in range(10000)):
        print(A)
        break
# 7