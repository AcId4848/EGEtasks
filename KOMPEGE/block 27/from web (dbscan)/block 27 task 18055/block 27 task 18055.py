f = open("27B_18055.txt")

data = []

for s in f:
    p = [float(c) for c in s.split()]
    data.append(p)
print(len(data))


def dist(p1, p2):
    x1, y1, h1, x2, y2, h2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def get_cluster(p0):
    cluster = [p for p in data if dist(p0, p) < 30]
    if len(cluster) > 0:
        for p in cluster: data.remove(p)
        next_cluster = [get_cluster(p) for p in cluster]
        cluster = cluster + sum(next_cluster, [])
    return cluster


clusters = []
while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + get_cluster(p0)
    print(len(cluster))
    clusters.append(cluster)

clusters = [kl for kl in clusters if len(kl) > 10] # удаление аномалий


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) * p1[2] for p1 in kl)
        m.append([sm, p])
    return min(m)[1]

centroid = [center(kl) for kl in clusters]
print(centroid)

K = len(centroid)
px = sum(x for x, y, h in centroid) / K
py = sum(y for x, y, h in centroid) / K
print(int(px*100000), int(py*100000))

# 25667971 24175730
# -1659383 -1838931