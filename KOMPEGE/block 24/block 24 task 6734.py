s = open("24_6734.txt").readline()

l = k = 0

m = 100000

for r in range(len(s)):
    if s[r] == ".":
        k += 1
    while k > 6:
        if s[l] == ".":
            k -= 1
        l += 1
    if k == 6:
        m = min(m, r-l+2)

print(m)

# 16