from turtle import *
f = open("27B_18052.txt")

data = []
for s in f:
    p = [float(c) for c in s.split()]
    data.append(p)
print(len(data))


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5


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


# visualization
up()
tracer(0)
colors = ["red", "green", "blue"] + ["black"] * 20
for kl, color in zip(clusters, colors):
    for x, y in kl:
        goto(x*50, y*50)
        dot(7, color)
update()
exitonclick()


clusters = [kl for kl in clusters if len(kl) > 10] # удаление аномалий

def m_ras(kl1, kl2):
    m = []
    for p1 in kl1:
        for p2 in kl2:
            m.append(dist(p1, p2))
    return [min(m), max(m)]


a = m_ras(clusters[0], clusters[1]) + m_ras(clusters[0], clusters[2]) +\
    m_ras(clusters[2], clusters[1])
print(int(min(a)*10000), int(max(a)*10000))

# 40112 103021
# 20063 94283