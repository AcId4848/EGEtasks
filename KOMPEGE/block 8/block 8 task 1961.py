from itertools import product

k = 1
for i in product("ЕЛМРУ", repeat=4):
    i = "".join(i)
    if i[0] == "Л":
        print(k, i)
    k += 1

# 126