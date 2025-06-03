def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for x in range(81234, 134689+1):
    d = div(x)
    if len(d) == 5:
        print(div(x))