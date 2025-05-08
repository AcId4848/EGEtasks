from itertools import product

a = []
for i in product("ВИШНЯ", repeat = 6):
    i = "".join(i)
    if i[0] != "Ш" and i[-1] != "И" and i[-1] != "Я" and i.count("В") <= 1:
        a.append(i)

print(len(a))
# 4352