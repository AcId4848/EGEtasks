def f1(x):
    return int("2" + x + x + "341011", 23)

def f2(x):
    return int("220" + x + "4", 23)

def f3(x):
    return int("110" + x + "6", 23)


for x in "0123456789ABCDEFGHIJKLM":
    if (f1(x) + f2(x) + f3(x)) % 22 == 0:
        print((f1(x) + f2(x) + f3(x)) / 22)
        break

# Correct answer: 7766124214
# Solved on the third try