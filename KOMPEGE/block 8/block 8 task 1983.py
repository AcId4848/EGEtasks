from itertools import product

array = []
for a in product("САЛО", repeat=6):
    if 0 < a.count("О") <= 3:
        array.append(a)

print(len(array))
# 3213