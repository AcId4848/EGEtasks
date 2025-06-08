f = open("26_2652.txt")
n = int(f.readline())
a = [int(x) for x in f]
a.sort()

count = len(set(a))
m = curr = 1
for i in range(1, len(a)):
    if a[i - 1] == a[i]:
        curr += 1
        m = max(m, curr)
    else:
        curr = 1

print(count, m)
# 108 383