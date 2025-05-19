from itertools import permutations

a = []
for i in permutations("ДЕЙКСТРА", 6):
    i = "".join(i).replace("Д", "C").replace("К", "С").replace("Т", "C").replace("Р", "С")
    print(i)
    if "ЙС" in i:
        a.append(i)

print(len(a))