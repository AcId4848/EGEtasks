def f1(x):
    return int("3" + x + "2" + x + "1" + x + "0" + x + "1", 19)


def f2(x):
    return int(x + "2024", 19)


def f3(x):
    return int("1" + x + "077", 19)


for x in "0123456789ABCDEFGHI":
    if (f1(x) + f2(x) + f3(x)) % 18 == 0:
        print((f1(x) + f2(x) + f3(x)) / 18)
