from itertools import product


k = 1
for i in product("АИМРЯ", repeat=4):
    i = "".join(i)
    if i == "АРИЯ":
        print(k, i)
    k += 1

# 85