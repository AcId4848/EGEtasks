s = open("7E659E.txt").readline()

k = m = l = 0

for r in range(len(s)):
    if s[r] == "X":
        k += 1
    while k > 140:
        if s[l] == "X":
            k -= 1
        l += 1
    m = max(m, r-l+1)

print(m)
# 211