def other_ch(x):
    s = ""
    while x != 0:
        s += str(x % 9)
        x //= 9
    return s[::-1]


def f(x):
    return 72070 + 7400 - x


max = 0
for x in range(1951):
    if other_ch(f(x)).count("0") > max:
        max = other_ch(f(x)).count("0")

print(max)