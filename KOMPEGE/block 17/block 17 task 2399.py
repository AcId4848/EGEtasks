s = [int(f) for f in open("17_2399.txt")]

s_35 = [int(x) for j in s if j % 35 == 0 for x in str(j)]
summary_35 = sum(s_35)
arr = []
for i in range(len(s)-1):
    if (s[i] > summary_35 and s[i+1] <= summary_35 and s[i+1] % 16 == 15 and s[i+1]//16%16 == 14) or \
        (s[i+1] > summary_35 and s[i] <= summary_35 and s[i] % 16 == 15 and s[i]//16%16 == 14):
            arr.append(s[i] + s[i+1])

print(len(arr), min(arr))
# 15 6410