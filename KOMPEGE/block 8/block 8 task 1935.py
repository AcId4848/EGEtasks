from itertools import permutations


a = []
for i in permutations("ВАЙФУ", 4):
    i = "".join(i)
    if i[0] != "Й" and "ВФ" not in i and "ФВ" not in i:
        a.append(i)

print(len(a))
# 68