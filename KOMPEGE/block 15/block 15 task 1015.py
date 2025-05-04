def f(x, y, A):
    return (x > 39) or (y > 26) or (2 * x + 4 * y < A)


for A in range(1000):
    if all(f(x, y, A) for x in range(1000) for y in range(1000)):
        print(A)
        break

# 183