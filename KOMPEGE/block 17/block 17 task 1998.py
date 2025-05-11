s = [int(f) for f in open("17_1998.txt")]

arr = []
for i in range(len(s)-2):
    if (s[i] * s[i+1] * s[i+2]) % 7 == 0 and  str(s[i] + s[i+1] + s[i+2])[-1] == "5":
        arr.append(s[i] + s[i+1] + s[i+2])


print(len(arr), max(arr))
# 153 19285