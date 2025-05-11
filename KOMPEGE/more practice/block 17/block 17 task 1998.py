a = [int(x) for x in open("17_1998.txt")]
ans = []

for i in range(len(a) - 2):
    if (a[i] * a[i+1] * a[i+2]) % 7 == 0 and (a[i] + a[i+1] + a[i+2]) % 10 == 5:
        ans.append(a[i] + a[i+1] + a[i+2])

print(len(ans), max(ans))