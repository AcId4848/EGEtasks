from itertools import product


a = []
for i in product("ABCD", repeat = 4):
    i = "".join(i)
    if i[0] <= i[1] <= i[2] <= i[3]:
        a.append(i)

print(len(a))