from itertools import product

array = []
for a in product("ПУЛЯ", repeat = 6):
    if a.count("У") == 2:
        array.append(a)

print(len(array))
# 1215
