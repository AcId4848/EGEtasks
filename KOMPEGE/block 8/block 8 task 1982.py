from itertools import product

array = []
for a in product("ЛОДКА", repeat=4):
    if a.count("О") >= 2:
        array.append(a)

print(len(array))
# 113