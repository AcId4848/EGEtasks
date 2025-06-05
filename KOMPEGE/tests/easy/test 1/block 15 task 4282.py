def f(x, y, z, A):
    return (150 != (y + 2 * x + 2 * z)) or (A < x) or (A < y) or (A < z)

for A in range(1000):
    if all(f(x, y, z, A) for x in range(1000) for y in range(100) for z in range(100)):
        print(A)