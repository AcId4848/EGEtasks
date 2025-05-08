from itertools import product

a = []
for i in product("ГЕПАРД",repeat = 5):
    i = "".join(i)
    if i[0] != "А" and i[-1] != "Е" and i.count("Г") == 1:
        a.append(i)

print(len(a))
# 2200