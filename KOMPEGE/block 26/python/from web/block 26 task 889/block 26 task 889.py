f = open("26_889.txt")
s, n = map(int, f.readline().split())
a = [int(x) for x in f]
b = []
for i in range(n):
    if 180 <= a[i] <= 200:
        b.append(a[i])
        a[i] = 0

