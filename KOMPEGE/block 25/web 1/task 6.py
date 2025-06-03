def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)


for x in range(850001, 850100):
    d = div(x)
    try:
        F = max(d) - min(d)
    except:
        F = 0
    if F != 0 and F % 3 == 0:
        print(x, F)
