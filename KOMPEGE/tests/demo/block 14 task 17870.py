def to7(x):
    s = ""
    while x != 0:
        s += str(x % 7)
        x //= 7
    return s[::-1]

for x in range(2030):
    if to7(7 ** 170 + 7 ** 100 - x).count("0") == 71:
        print(x)
# 2029