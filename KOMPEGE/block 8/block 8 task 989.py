from itertools import product

k = 1
for i in product("АИМРЯ", repeat = 4):
    i = "".join(i)
    if k == 211:
        print(k, i)
    k += 1
# ИРМА