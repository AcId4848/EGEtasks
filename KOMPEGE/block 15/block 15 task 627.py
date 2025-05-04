def f(x, y, A):
    return (x * y > A) and (x > y) and (x < 8)


for A in range(1, 1000):
    if all(f(x, y, A) == 0 for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
# 42