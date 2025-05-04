def f(x):
    s = ""
    while x != 0:
        s += "0123456789AB"[x % 12]
        x //= 12
    return s[::-1]


print(int(f(15), 12))
print(f(6 * 144 ** 26 + 11 * 12 ** 75 - 48).count("B"))
# 51