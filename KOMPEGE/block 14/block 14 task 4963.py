def f(x, y):
    return int("123" + x + "5", 15) + int("67" + y + "9", 17)


for y in "0123456789ABCDEFG":
    for x in "0123456789ABCDE":
        if f(x, y) % 131 == 0:
            print(f(x, y) / 131)
# 686