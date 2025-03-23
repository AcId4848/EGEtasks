clustersA = [[], [], []]

for s in open("27A_19747.txt"):
    x, y = [float(c) for c in s.split()]
    if x > 5 and y > 5:
        clustersA[0].append([x, y])
    elif x < 5:
        clustersA[1].append([x, y])
    else:
        clustersA[2].append([x, y])

# print([len(kl) for kl in clustersA])

clustersB = [[], [], [], [], []]

for s in open("27B_19747.txt"):
    x, y = [float(c) for c in s.split()]
    if 10 < x < y:
        clustersB[0].append([x, y])
    elif x < y < 10:
        clustersB[1].append([x, y])
    elif 10 > x > y:
        clustersB[2].append([x, y])
    elif x > 10 > y:
        clustersB[3].append([x, y])
    else:
        clustersB[4].append([x, y])

# print([len(kl) for kl in clustersB])


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

pxA = sum(x for x, y in centerA) / len(centerA) * 100000
pyA = sum(y for x, y in centerA) / len(centerA) * 100000

print(int(pxA), int(pyA))

pxB = sum(x for x, y in centerB) / len(centerB) * 100000
pyB = sum(y for x, y in centerB) / len(centerB) * 100000

print(int(pxB), int(pyB))

# 532496 533164
# 1091104 954833