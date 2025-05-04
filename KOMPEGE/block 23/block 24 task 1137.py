def f(c, e):
    if int(c, 2) > int(e, 2):
        return 0
    if c == e:
        return 1
    if int(c, 2) < int(e, 2):
        return f(bin(int(c, 2) + 1)[2:], e) + f(c + "0", e) + f(c + "1", e)

print(f("100", "11101"))
# 79
