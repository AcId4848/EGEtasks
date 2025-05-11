s = [int(f) for f in open("17_2310.txt")]

s_4 = [j for j in s if j % 4 == 0]
sum_4 = min(s_4) + max(s_4)

arr = []
for i in range(len(s)-1):
    if s[i] + s[i+1] < sum_4:
        arr.append(s[i] + s[i+1])

print(len(arr), max(arr))