def f(x):
    s = ""
    while x != 0:
        s += str(x % 4)
        x //= 4
    return s[::-1]

print(f(3 * 16 ** 8 - 4 ** 5 + 3).count("3"))
# 12
