def f(x):
    s = ""
    while x != 0:
        s += str(x % 5)
        x //= 5
    return s[::-1]


for x in range(10000):
    if (f(125 ** 200 - 5 ** x + 74)).count("4") == 100:
        print(x)
        break
# 502