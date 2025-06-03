import math

for n in range(400000000, 600000000):
    de = [d for d in range(2, n-1) if n % d == 0]
    if len(de) < 5:
        pn = 0
    else:
        pn = math.prod(de[:5])
    if pn % 100 == 17 and pn <= n:
        print(pn, de[4])
