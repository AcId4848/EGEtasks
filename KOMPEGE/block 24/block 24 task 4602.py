# from re import *
#
s = open("24_4602.txt").readline()
#
# reg = r"(?=(([BCD]|[AO])+))"
#
# # print(s[50:])
# # print([x.group(1) for x in finditer(reg, s[50:])])
# print(max(len(x.group(1)) for x in finditer(reg, s)))

s = s.replace("BA", "*").replace("BO", "*").replace("CA", "*").replace("CO", "*").replace("DA", "*").replace("DO", "*")


arr = []
k = 0
for i in s:
    if i == "*":
        k += 1
    else:
        arr.append(k)
        k = 0
print(max(arr))
# 174