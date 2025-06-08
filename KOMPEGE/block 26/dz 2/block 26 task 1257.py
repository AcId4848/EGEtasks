f = open("26_1257.txt")

n = int(f.readline())
a = [int(x) for x in f]
a.sort()
d = set(a)
ans = []
for i in range(n):
    for j in range(i + 1, n):
        if a[i] % 2 != a[j] % 2 and a[i] + a[j] in d:
            ans.append(a[i]+a[j])

print(len(ans), max(ans))
