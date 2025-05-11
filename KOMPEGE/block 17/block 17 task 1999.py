s = [int(f) for f in open("17_1999.txt")]

arr = []
for i in range(len(s)-2):
    if (s[i] % 12 == 0 or s[i+1] % 12 == 0 or s[i+2] % 12 == 0) and (s[i] % 3 == 0 and s[i+1] % 3 == 0 and s[i+2] % 3 == 0):
        arr.append(int((s[i] + s[i+1] + s[i+2]) // 3))

print(len(arr), min(arr))
# 119 -7213