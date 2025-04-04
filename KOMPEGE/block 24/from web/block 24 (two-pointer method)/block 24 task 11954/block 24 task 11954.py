s = open("24_11954.txt").readline()

kx = ky = 0
m = 100000000
l = 0

for r in range(len(s)):
    if s[r] == "X":
        kx += 1
    if s[r] == "Y":
        ky += 1

    while kx >= 500 or ky == 1:
        if s[l] == "X":
            kx -= 1
        if s[l] == "Y":
            ky -= 1
        l += 1
        if kx == 500 and ky == 0:
            m = min(m, r-l+1)
print(m)

# 68500
