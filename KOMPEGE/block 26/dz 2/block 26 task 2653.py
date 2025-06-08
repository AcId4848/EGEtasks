f = open("26_2653.txt")

n = int(f.readline())
a = [int(x) for x in f]
a.sort()
weight = [0] * (sum(a) + 1)
s = 0
for x in a:
    weight2 = weight.copy()
    for i in range(s + 1):
        if weight[i] == 1:
            weight2[i + x] = 1
    weight2[x] = 1
    weight = weight2
    s += x
k, m = 0, 0
for i in range(1, sum(a) + 1):
    if weight[i] == 0:
        k += 1
        m = i

print(k, m)