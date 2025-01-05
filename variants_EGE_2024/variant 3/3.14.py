def f1(x):
    return int("1" + x + "2" + x + "3" + x + "4" + x + "5", 25)


def f2(x):
    return int("2" + x + "024", 25)


def f3(x):
    return int("1" + x + "099", 25)


for x in "0123456789ABCDEFGHIJKLMNO":
    if (f1(x) + f2(x) + f3(x)) % 24 == 0:
        print((f1(x) + f2(x) + f3(x)) / 24)

# Correct answer: 11727433732
# Solved on the first try