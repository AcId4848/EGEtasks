clustersA = [[], []]

for s in open("27A_18626.txt"):
    x, y = [float(c) for c in s.split()]
    if y < 0 and x < 2:
        pass
    elif x > 4 and y > 6:
        pass
    elif x < 2 or (x < 4 and y > 6) or (x < 4 and y < 3):
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

# print([len(kl) for kl in clustersA])

clustersB = [[], [], []]

for s in open("27B_18626.txt"):
    x, y = [float(c) for c in s.split()]
    if x < 2 and y < 2:
        pass
    elif x > 9 and y > 9:
        pass
    elif 7 < x < 8 and 4 < y < 6:
        pass
    elif x < 4:
        clustersB[0].append([x, y])
    elif y < 2 or (x > 7 and y < 7.5):
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

pxA = sum(x for x, y in centerA) / len(centerA) * 100000
pyA = sum(y for x, y in centerA) / len(centerA) * 100000

print(int(pxA), int(pyA))

pxB = sum(x for x, y in centerB) / len(centerB) * 100000
pyB = sum(y for x, y in centerB) / len(centerB) * 100000

print(int(pxB), int(pyB))

# 358310 347120
# 507819 522848