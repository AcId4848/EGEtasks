s = open("24_1039.txt").readline()
m = [1] * len(s)

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        m[i] = m[i-1]+1
        if m[i] == 4:
            print(s[i], m[i])

print(max(m))

# 4