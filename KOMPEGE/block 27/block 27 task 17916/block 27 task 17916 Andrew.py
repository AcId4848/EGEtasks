def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def centr(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]

clasterA = [[], []]
clasterB = [[], [], [], [], []]

for s in open("27_A_17916.txt"):
    x, y = [float(c) for c in s.replace(",",".").split()]
    if y > 8:
        clasterA[0].append([x, y])
    else:
        clasterA[1].append([x, y])

for s in open("27_B_17916.txt"):
    x, y = [float(c) for c in s.split()]
    if y > 14:
        clasterB[0].append([x, y])
    elif y > 10:
        clasterB[1].append([x, y])
    elif y > 5.9:
        clasterB[2].append([x, y])
    elif x < 10:
        clasterB[3].append([x, y])
    else:
        clasterB[4].append([x, y])


CentrA = [centr(kl) for kl in clasterA]
CentrB = [centr(kl) for kl in clasterB]

PxA = sum(x for x, y in CentrA) / 2 * 10000
PyA = sum(y for x, y in CentrA) / 2 * 10000

print(int(PxA), int(PyA))

PxB = sum(x for x, y in CentrB) / 5 * 10000
PyB = sum(y for x, y in CentrB) / 5 * 10000

print(int(PxB), int(PyB))