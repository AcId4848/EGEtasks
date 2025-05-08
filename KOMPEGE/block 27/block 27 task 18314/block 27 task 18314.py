clustersA = [[], []]

for s in open("27_A_18314.txt"):
    x, y = [float(c) for c in s.split()]
    if x < 23:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

clustersB = [[], [], []]

for s in open("27_B_18314.txt"):
    x, y = [float(c) for c in s.split()]
    if x > 20:
        clustersB[0].append([x, y])
    elif y > -5:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return abs(x2 - x1) + abs(y2 - y1)


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]


centerA = [center(kl) for kl in clustersA]
centerB = [center(kl) for kl in clustersB]

pxA = sum(x for x, y in centerA) / 2 * 1000
pyA = sum(y for x, y in centerA) / 2 * 1000
print(int(pxA), int(pyA))

pxB = sum(x for x, y in centerB) / 3 * 1000
pyB = sum(y for x, y in centerB) / 3 * 1000
print(int(pxB), int(pyB))

# 23509 554
# 3078 -4758