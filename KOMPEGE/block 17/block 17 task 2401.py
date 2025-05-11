s = [int(f) for f in open("17_2401.txt")]

arr = []
for i in range(len(s) - 1):
    if 50 < abs(s[i]) + abs(s[i+1]) < 200:
        arr.append(min(s[i], s[i+1]))

print(len(arr), min(arr))
# 1 -92