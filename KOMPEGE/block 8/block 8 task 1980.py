from itertools import product


a = []
for i in product("ABCWXYZ", repeat = 6):
    s = "".join(i)
    if s[0] in "WXYZ" and s[-1] in "WXYZ" and s.count("W") + s.count("X") + s.count("Y") + s.count("Z") == 2:
        print(s)
        a.append(s)

print(len(a))