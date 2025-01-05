def f1(x):
    return int(("1" + x)*4 + "1", 23)


def f2(x):
    return int("20" + x + "24", 23)


def f3(x):
    return int("1" + x + "235", 23)


for x in "0123456789ABCDEFGHIJKLM":
    if (f1(x) + f2(x) + f3(x)) % 22 == 0:
        print((f1(x) + f2(x) + f3(x)) / 22)
        break

# Correct answer: 4651779499
# Solved on the first try

