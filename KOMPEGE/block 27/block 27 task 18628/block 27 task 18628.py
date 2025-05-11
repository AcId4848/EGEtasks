clustersA = [[], []]

for s in open("27A_18628.txt"):
    x, y = [float(c) for c in s.split()]
    if y > 2 * x:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

# print(len(clustersA[0]))

clustersB = [[], [], []]

for s in open("27B_18628.txt"):
    x, y = [float(c) for c in s.split()]
    if (x < 0 and y > 3.5) or (x >= 0 and y > x + 3.5):
        clustersB[0].append([x, y])
    elif x < 0:
        clustersB[1].append([x, y])
    elif x > 0:
        clustersB[2].append([x, y])

# print(len(clustersB[0]))


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]


centerA = [center(kl) for kl in clustersA]
centerB = [center(kl) for kl in clustersB]

pxA = sum(x for x, y in centerA) / 2 * 100000
pyA = sum(y for x, y in centerA) / 2 * 100000

print(int(pxA), int(pyA))

pxB = sum(x for x, y in centerB) / 3 * 100000
pyB = sum(y for x, y in centerB) / 3 * 100000

print(int(pxB), int(pyB))

# 258853 499656
# 6165 372336