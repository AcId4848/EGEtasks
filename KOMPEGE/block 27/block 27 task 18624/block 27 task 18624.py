clustersA = [[], []]

for s in open("27A_18624.txt"):
    x, y = [float(c) for c in s.split()]
    if x < 4 or (y < 6 and x < 6):
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

clustersB = [[], [], []]

for s in open("27B_18624.txt"):
    x, y = [float(c) for c in s.split()]
    if x < 1 or (x < 4 and y < 2):
        clustersB[0].append([x, y])
    elif x < 7 and y < 5:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])


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

# 455058 449904
# 366751 398174