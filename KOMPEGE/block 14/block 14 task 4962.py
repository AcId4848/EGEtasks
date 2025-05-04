def f(x):
    return int("55" + x + "87", 14)


def f1(x):
    return int("3364" + x, 11) + int(x + "7946", 12) == f(x)

for x in "0123456789A":
    if f1(x):
        print(f(x))

# 207291