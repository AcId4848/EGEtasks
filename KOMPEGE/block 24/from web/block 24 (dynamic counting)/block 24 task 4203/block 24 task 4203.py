s = open("24_4203.txt").readline()
m = [0] * len(s)

for i in range(len(s)):
    if s[i-1] + s[i] == "AB" or s[i-1] + s[i] == "CB":
        m[i] = m[i-2] + 1
    if m[i] == 65:
        print(s[i-64:i+1])
print(max(m))
# 65