def f(x):
    s = ""
    while x != 0:
        s += str(x % 6)
        x //= 6
    return s[::-1]


print(f(5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875).count("5") - f(5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875).count("0"))
# 1182
