s = open("24_3375.txt").readline()
m = [0] * len(s)

for i in range(1, len(s)):
    if s[i-1] + s[i] == "AA" or s[i-1] + s[i] == "CC":
        m[i] = m[i-2] + 1
print(max(m))
# 5