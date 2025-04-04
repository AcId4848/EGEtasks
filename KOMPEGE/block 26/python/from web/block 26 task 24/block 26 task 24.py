f = open("26_24.txt")
s, n = map(int, f.readline().split())
a = [int(x) for x in f]
a.sort()

s1 = 0
b = 0
k = 0
for i in range(n):
    if s1 + a[i] <= s:
        s1 += a[i]
        b = a[i]
        k += 1
        a[i] = 0
for i in range(n):
    if a[i] != 0 and s1 - b + a[i] <= s:
        s1 = s1- b + a[i]
        b, a[i] = a[i], b

print(k, b)

# 568 50