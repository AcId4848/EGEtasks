def f(x, y, A):
    return (x ** 2 - 10 * x + 16 > 0) or (y ** 2 - 10 * y + 21 > 0) or (x * y < 2 * A)


for A in range(1000):
    if all(f(x, y, A) for x in range(1000) for y in range(1000)):
        print(A)
        break

# 29