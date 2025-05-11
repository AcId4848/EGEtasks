from math import prod

for m in range(1, 1000):
    m = str(m)
    p1 = 2 * prod([int(i) for i in m if int(i) % 2 == 0 and int(i) != 0])
    p2 = 1 * prod([int(j) for j in m if int(j) % 2 == 1])
    r = abs(p1 - p2)
    if r == 29:
        print(m)
        break

# 238