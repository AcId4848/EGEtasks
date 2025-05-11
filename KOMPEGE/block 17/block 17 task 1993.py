s = [f for f in open("17_1993.txt")]

arr = []
for i in range(len(s)-1):
    if (int(s[i]) + int(s[i+1])) % 3 == 0 and (int(s[i]) + int(s[i+1])) % 6 != 0 and str(int(s[i]) * int(s[i+1]))[-1] == "8":
        arr.append(int(s[i]) + int(s[i+1]))

print(len(arr), max(arr))
# 140 17031