f = open("27_B_17882.txt")
data = []
for s in f:
    p = [float(c) for c in s.split()]
    data.append(p)

print(len(data))


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def get_cluster(p0):
    cluster = [p for p in data if dist(p0, p) < 1]
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

K = len(clusters)

def center(kl):
    m = []
    for p in kl:
        s = sum(dist(p, p1) for p1 in kl)
        m.append([s, p])
    return min(m)[1]


centroid = [center(kl) for kl in clusters]
print(centroid)


px = sum(x for x, y in centroid) / K * 10000
py = sum(y for x, y in centroid) / K * 10000
print(int(px), int(py))

# 10738 30730
# 37522 51277
