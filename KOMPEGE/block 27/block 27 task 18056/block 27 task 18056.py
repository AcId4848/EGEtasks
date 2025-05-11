a = open("27A_18056.txt")
b = open("27B_18056.txt")

data_a = []
data_b = []

for s in a:
    p = [float(c) for c in s.split()]
    data_a.append(p)
print(len(data_a))

for s in b:
    p = [float(c) for c in s.split()]
    data_b.append(p)
print(len(data_b))


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def get_cluster(p0, data):
    cluster = [p for p in data if dist(p0, p) <= 0.9]
    if len(cluster) > 0:
        for p in cluster:
            data.remove(p)
        next_cluster = [get_cluster(p, data) for p in cluster]
        cluster = cluster + sum(next_cluster, [])
    return cluster

clustersA = []
clustersB = []

while len(data_a) > 0:
    p0 = data_a.pop()
    cluster = [p0] + get_cluster(p0, data_a)
    clustersA.append(cluster)

while len(data_b) > 0:
    p0 = data_b.pop()
    cluster = [p0] + get_cluster(p0, data_b)
    clustersB.append(cluster)


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]


print([len(kl) for kl in clustersA])
print([len(kl) for kl in clustersB])
centerA = [center(kl) for kl in clustersA]
centerB = [center(kl) for kl in clustersB]


px = sum(x for x, y in centerB[:3]) / 3 * 100000
py = sum(y for x, y in centerB[:3]) / 3 * 100000

print(int(px), int(py))

# [47, 43, 4, 6]
# [3330, 3328, 3329, 5, 3, 4]

print(centerA, centerB)

# 43744 47901
# 99895 100091