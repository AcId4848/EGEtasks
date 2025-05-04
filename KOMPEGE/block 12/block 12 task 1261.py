from itertools import product


array = []
for s in product(["1", "2"], repeat = 16):
    s = "".join(s)
    if s.count("1") == 12 and s.count("2") == 4:
        while "11" in s:
            if "112" in s:
                s = s.replace("112", "7", 1)
            else:
                s = s.replace("11", "3", 1)
        array.append([sum([int(i) for i in s]), s])

print(max(array))
# 34