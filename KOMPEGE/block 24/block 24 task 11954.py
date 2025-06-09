# s = open("24_11954.txt").readline()
#
# k = l = 0
# m = 100000000
#
# for r in range(len(s)):
#     if s[r] == "Y":
#         k = 0
#         l = r+1
#     if s[r] == "X":
#         k += 1
#     while k >= 500:
#         m = min(m, r - l + 1)
#         if s[l] == "X":
#             k -= 1
#         l += 1
#
#
# print(m)


s = open("24_11954.txt").readline()
m = 100000
r = 0
l = 0
for r in range(m, len(s)):
    c = s[l:r]
    if "Y" in c:
        l = r + 1
    while c.count("X") > 500:
        l += 1
        c = s[l:r]
    if c.count("X") == 500 and "Y" not in c:
        m = min(m, len(c))

print(m)