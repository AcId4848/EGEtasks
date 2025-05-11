s = [int(f) for f in open("17_2400.txt")]

arr = []
for i in range(len(s)-1):
    if s[i] + s[i+1] >= 100 and (s[i] < 0 or s[i+1] < 0):
        arr.append(s[i] * s[i+1])

print(len(arr), max(arr))
# 1137 -2655