s = open("24_3163.txt").readline()
m = [1] * len(s)

for i in range(1, len(s)):
    if s[i - 1] + s[i] != "ST":
        m[i] = m[i-1] + 1
print(max(m))

# 6578