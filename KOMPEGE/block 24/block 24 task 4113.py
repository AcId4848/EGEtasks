s = open("24_4113.txt").readline()

m = [0] * len(s)

for i in range(1, len(s)):
    if s[i - 1] + s[i] == "BB" or s[i - 1] + s[i] == "DD":
        m[i] = m[i - 2] + 1
print(max(m))
print(m)
# 317
