s = open("24_11954.txt").readline()

k = l = 0
m = 100000000

for r in range(len(s)):
    if s[r] == "Y":
        k = 0
        l = r+1
    if s[r] == "X":
        k += 1
    while k >= 500:
        m = min(m, r - l + 1)
        if s[l] == "X":
            k -= 1
        l += 1


print(m)