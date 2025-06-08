f = open("26_813.txt")

s, n = map(int, f.readline().split())
a = [int(x) for x in f]
a.sort()
b = []

while sum(b) + a[0] <= s:
    for i in range(len(a)-1, 0, -1):
        if sum(b) + a[i] <= s:
            b += [a.pop(i)]
            break
    if sum(b) + a[0] <= s:
        b += [a.pop(0)]

print(len(b), b[-1])

# 573 229