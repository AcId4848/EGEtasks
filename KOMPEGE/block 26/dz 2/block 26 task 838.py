f = open("26_838.txt")

n = int(f.readline())
a = [int(x) for x in f]
a.sort()
d1 = []
d2 = []
d1 += [a.pop(-1)]

while len(a) > 0:
    d1 += [a.pop(-1)]
    while sum(d2) <= sum(d1):
        d2 += [a.pop(0)]

print(len(d1), len(d2))
# 2054 4612