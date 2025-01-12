clustersA = [[], []]

for s in open("27.13.A_19567.txt"):
    x, y = [float(c) for c in s.split()]
    if y < 0:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

clustersB = [[], [], [], [], [], []]

# for s in open("27.13.B_19567.txt"):
#     x, y = [float(c) for c in s.split()]
#     if


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

pxA = sum(x for x, y in centerA) / 2 * 10000
pyA = sum(y for x, y in centerA) / 2 * 10000
print(int(pxA), int(pyA))