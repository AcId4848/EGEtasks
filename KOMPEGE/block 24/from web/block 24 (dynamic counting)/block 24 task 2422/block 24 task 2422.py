s = open("24_2422.txt").readline()
m = [1] * len(s)

for i in range(1, len(s)):
    if s[i] >= s[i-1]:
        m[i] = m[i-1]+1
        if m[i] == 15:
            print(s[i-14:i+1])
print(max(m))

# 15

