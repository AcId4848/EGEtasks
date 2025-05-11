s = [int(f) for f in open("17_2239.txt")]
maxim_19 = max([j for j in s if j % 19 == 0])

arr = []
for i in range(len(s)-1):
    if s[i] > maxim_19 or s[i+1] > maxim_19:
        arr.append(s[i] + s[i+1])

print(len(arr), min(arr))
# 34 11169