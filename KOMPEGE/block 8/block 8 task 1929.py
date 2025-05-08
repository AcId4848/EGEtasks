from itertools import permutations


a = []
for s in permutations("ДЕЙКСТРА", 6):
    s = "".join(s)
    if ("ЙД" in s or "ЙК" in s or "ЙС" in s or "ЙТ" in s or "ЙР" in s) and s.count("Й") == 1:
        a.append(s)

print(len(a))
# 9000