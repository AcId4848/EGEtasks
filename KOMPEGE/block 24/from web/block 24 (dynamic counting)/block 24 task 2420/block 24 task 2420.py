s = open("24_2420.txt").readline()
m = [0]*len(s)

for i in range(len(s)):
    if s[i] in "ABEF":
        m[i] = m[i-1] + 1
    # else:
    #     m[i] = 0

print(max(m))

# 20