s = [int(f) for f in open("17_2238.txt")]

arr = []
for i in range(len(s)-2):
    if len([j for j in [s[i], s[i+1], s[i+2]] if j > (sum(s) / len(s))]) >= 2:
        arr.append(sum([s[i], s[i+1], s[i+2]]))

print(len(arr), max(arr))
# 5020 28715