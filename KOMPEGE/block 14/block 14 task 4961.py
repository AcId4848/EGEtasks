def f(x):
    return int("9759" + x, 17) + int("3" + x + "108", 17)

for x in "0123456789ABCDEFG":
    if f(x) % 11 == 0:
        print(f(x) / 11)

# 95306