s = open("24_12476.txt").readline()

l = m = k = 0


for r in range(1, len(s)):
    if r >= 2 and (s[r-2] + s[r-1] + s[r] == "ORO" or s[r-2] + s[r-1] + s[r] == "ROR"):
        k = 0
        l = r-1
    if s[r - 1] + s[r] == "RO":
        k += 1
    while k > 21:
        if s[l] + s[l + 1] == "RO":
            k -= 1
        l += 1
    if k == 21:
        m = max(m, r-l+1)
print(m)

# 814