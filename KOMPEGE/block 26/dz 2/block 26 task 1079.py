f = open("26_1079.txt")

n = int(f.readline())
a = [int(x) for x in f]
a.sort()
ans = []
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % 2 == 0:
            sr = (a[i] + a[j]) // 2
            if a[2499] < sr < a[3750]:
                ans.append(sr)

print(len(ans), min(ans))
# 2405042 546772
