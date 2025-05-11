f = open("27B_18677.txt")

data = []

for s in f:
    p = [float(c) for c in s.split()]
    data.append(p)
print(len(data))


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) < 0.9]
    if len(cluster) > 0:
        for p in cluster:
            data.remove(p)
        next_cluster = [get_cluster(p) for p in cluster]
        cluster = cluster + sum(next_cluster, [])
    return cluster

clusters = []

while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + get_cluster(p0)
    print(len(cluster))
    clusters.append(cluster)


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]


centroid = [center(kl) for kl in clusters]
K = len(centroid) - 3

px = sum(x for x, y in centroid[:3]) / K * 100000
py = sum(y for x, y in centroid[:3]) / K * 100000

print(int(px), int(py))
# 528073 71781
# 669946 370701