s = open("24_4643.txt").readline()
s = s.replace("B", "A").replace("2", "1")

m = [0] * len(s)

for i in range(2, len(s)):
    if s[i-2] + s[i-1] + s[i] == "11A":
        m[i] = m[i-3] + 1
print(max(m))

# 67