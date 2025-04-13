clustersA = [[], []]

for s in open("27A_18051.txt"):
    x, y = [float(c) for c in s.split()]
    if x < 1.05:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

clustersB = [[], [], []]

for s in open("27B_18051.txt"):
    x, y = [float(c) for c in s.split()]
    if y > 0.8 and x < 7.95:
        clustersB[0].append([x, y])
    elif x > 8.95 and y > 0:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]


centerA = [center(kl) for kl in clustersA]
centerB = [center(kl) for kl in clustersB]

pxA = sum(x for x, y in centerA) / 2 * 10000
pyA = sum(y for x, y in centerA) / 2 * 10000
print(int(pxA), int(pyA))

pxB = sum(x for x, y in centerB) / 3 * 10000
pyB = sum(y for x, y in centerB) / 3 * 10000
print(int(pxB), int(pyB))

# 10410 66711
# 81775 7384