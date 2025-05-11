clustersA = [[], []]

for s in open("27A_18676.txt"):
    x, y = [float(c) for c in s.split()]
    if y > x * 2 - 9.5:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

# print(len(clustersA[1]))

clustersB = [[], [], []]

for s in open("27B_18676.txt"):
    x, y = [float(c) for c in s.split()]
    if x < 3.5 or (x >= 3.5 and y > x - 1):
        clustersB[0].append([x, y])
    elif y < 0 or y <= x * 2 - 13:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])

# print(len(clustersB[2]))


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

# 566258 38951
# 591893 290926