def f(x):
    s = ""
    while x != 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]


print(f(9 ** 11 * 3 ** 20 - 3 ** 9 - 27).count("2"))