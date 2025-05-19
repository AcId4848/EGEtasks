clustersA = [[], [], [], []]

for s in open("27A_20295.txt"):
    x, y = [float(c) for c in s.split()]
    if x < 0 and y > 0:
        clustersA[0].append([x, y])
    elif x < 1 and y < 0:
        clustersA[1].append([x, y])
    elif y > 1.5 and x > 2:
        clustersA[2].append([x, y])
    else:
        clustersA[3].append([x, y])

clustersB = [[], [], [], [], [], [], []]

for s in open("27B_20295.txt"):
    x, y = [float(c) for c in s.split()]
    if x < -4:
        clustersB[0].append([x, y])
    elif 4 > x > 1 and y > -2:
        clustersB[1].append([x, y])
    elif 4 > x > 1 and y < -2:
        clustersB[2].append([x, y])
    elif 6 > x > 1 and y > 1:
        clustersB[3].append([x, y])
    elif 6 > x > 1 and y < 1:
        clustersB[4].append([x, y])
    elif x > 6 and y > 3:
        clustersB[5].append([x, y])
    else:
        clustersB[6].append([x, y])

def dist(p, p1):
    x1, y1, x2, y2 = *p, *p1
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
        return min(m)[1]


centerA = [center(kl) for kl in clustersA]
centerB = [center(kl) for kl in clustersB]

pxA = min(centerA)
pA = (centerA)
print(pxA)
