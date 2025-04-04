s = open("24_7662.txt").readline()

l = m = kSOLO = 0
d = {x:0 for x in "0123456789"}

for r in range(3, len(s)): # we can do that because the first three characters are letters.
    if s[r-3] + s[r-2] + s[r-1] + s[r] == "SOLO":
        kSOLO += 1
    if s[r] in "0123456789":
        d[s[r]] += 1
    while kSOLO > 4:
        if s[l] + s[l+1] + s[l+2] + s[l+3] == "SOLO":
            kSOLO -= 1
        if s[l] in "0123456789":
            d[ s[l] ] -= 1
        l += 1
    if sum(d[x] > 0 for x in "0123456789") >= 5:
        m = max(m, r-l+1)
print(m)

# 431