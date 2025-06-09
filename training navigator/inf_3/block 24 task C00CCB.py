s = open("C00CCB.txt").readline()

l = k = m = 0

for r in range(len(s)):
    if "W" == s[r]:
        k += 1
    while k > 130:
        if "W" == s[l]:
            k -= 1
        l += 1
    m = max(m, r-l+1)

print(m)
# 237