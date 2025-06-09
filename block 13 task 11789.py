def d(x, y):
    return (3 * x + 2 * y > 25) or (x > 2 * y) or (x + 4 * y < a)


for a in range(1000):
    if any(d(x, y) == 0 for x in range(1000) for y in range(1000)):
        print(a)