s = open("24_12476.txt").readline()

kRO = l = m = 0
for r in range(1, len(s)):
    if "ORO" in s[l:r+1] or "ROR" in s[l:r+1]:
        l = r
        kRO = 0

    if s[r-1:r+1] == "RO":
        kRO += 1
    while kRO > 21:
        if s[l:l+2] == "RO":
            kRO -= 1
        l += 1
    if kRO == 21:
        m = max(m, r-l+1)
print(m)
# 814