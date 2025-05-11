s = [int(f) for f in open("17_2002.txt")]

arr = []
for i in range(len(s)-3):
    if [s[i], s[i+1], s[i+2], s[i+3]] == sorted([s[i], s[i+1], s[i+2], s[i+3]])[::-1] and s[i] - s[i+3] > 1000:
        arr.append(sum([s[i], s[i+1], s[i+2], s[i+3]]))

print(len(arr), min(arr))
# 181 -31478