s = [int(f) for f in open("17_2398.txt")]


arr = []
for i in range(len(s)-2):
    if not (s[i] > 0 and s[i] % 10 == 9) and s[i+1] > 0 and s[i+1] % 10 == 9 and not (s[i+2] > 0 and s[i+2] % 10 == 9):
        arr.append(sum([s[i], s[i+1], s[i+2]]))

print(len(arr), max(arr))