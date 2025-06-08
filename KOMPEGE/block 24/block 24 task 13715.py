s = open("24_13715.txt").readline()

l = m = k = 0

for r in range(1, len(s)):
    if s[r-1] + s[r] == "AB":
        k += 1
    while k > 50:
        if s[l] + s[l+1] == "AB":
            k -= 1
        l += 1
    if k == 50:
        m = max(m, r-l+1)

print(m)
# 13715
