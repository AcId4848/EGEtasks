a = [int(x) for x in open("17_1993.txt")]
ans = []
for i in range(len(a) - 1):
    if (a[i] + a[i+1]) % 3 == 0 and (a[i] + a[i+1]) % 6 != 0  and abs(a[i] * a[i+1]) % 10 == 8:
        ans.append(a[i] + a[i+1])

print(len(ans), max(ans))

