from itertools import product

k = 1
for i in product("АГИЛМОРТ", repeat = 4):
    i = "".join(i)
    if i[-2:] == "ИМ":
        print(k, i)
    k += 1

# 4053