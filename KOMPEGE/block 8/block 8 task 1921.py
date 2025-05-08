from itertools import product

a = []
for i in product("0123456789", repeat = 3):
    i = [int(s) for s in i]
    if i[0] <= i[1] <= i[2] and i[0] != 0:
        a.append(i)

print(len(a))
# 165