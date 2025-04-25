from itertools import product

a = []
for i in product("КРЕСЛО", repeat = 4):
    s = "".join(i)
    if s[0] in "КРСЛ" and s[-1] in "ЕО":
        a.append(s)
print(len(a))


