clustersA = [[], []]

for s in open("27A_18630.txt"):
    x, y = [float(c) for c in s.split()]
    if 4 < x < 8 < y:
        pass
    elif 4 < x < 8 and y < 2:
        pass
    elif x < 4:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

# print([len(kl) for kl in clustersA])

clustersB = [[], [], []]

for s in open("27B_18630.txt"):
    x, y = [float(c) for c in s.split()]
    if 8 < y < 10 and x < 3:
        pass
    elif 5 < x < 8 and 7 < y < 9:
        pass
    elif x > 14 and 7 < y < 9:
        pass
    elif y > 8:
        clustersB[0].append([x, y])
    elif x < 9:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])

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


pxA = sum(x for x, y in centerA) / 2 * 100000
pyA = sum(y for x, y in centerA) / 2 * 100000

print(int(pxA), int(pyA))

pxB = sum(x for x, y in centerB) / 3 * 100000
pyB = sum(y for x, y in centerB) / 3 * 100000

print(int(pxB), int(pyB))

# 559397 625605
# 923413 613488