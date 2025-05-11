s = [int(f) for f in open("17_2403.txt")]

arr = []
for i in range(len(s)-1):
    if (s[i] % 9 == 0 and s[i+1] % 9 != 0 and s[i+1] % 8 == 3) or (s[i+1] % 9 == 0 and s[i] % 9 != 0 and s[i] % 8 == 3):
       arr.append(max(s[i], s[i+1]))

print(len(arr), max(arr))