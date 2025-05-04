def f(x):
    s = ""
    while x != 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]

print(f(2 * 27 ** 7 + 3 ** 10 - 9).count("0"))
# 13