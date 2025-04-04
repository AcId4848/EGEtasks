s = open("24_7043.txt").readline()

l = 0
m = 1000000
d = {x:0 for x in "0123456789ABCDEF"}

for r in range(len(s)):
    if s[r] in "0123456789ABCDEF":
        d[s[r]] += 1
    while all(d[x] > 0 for x in "0123456789ABCDEF"):
        if s[l] in "0123456789ABCDEF":
            d[s[l]] -= 1
        l += 1
        if all(d[x]>0 for x in "0123456789ABCDEF"):
            m = min(m, r-l+1)
print(m)
# 42