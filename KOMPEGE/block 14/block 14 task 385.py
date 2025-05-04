def f(x):
    s = ""
    while x != 0:
        s += str(x % 5)
        x //= 5
    return s[::-1]


print(len([i for i in range(1000) if len(f(i)) <= 4 and len(bin(i)[2:]) >= 5 and hex(i)[-1] == "c"]))
# 38
# print([[len(f(i)) <= 4, len(bin(i)) >= 5, hex(i)[-1] == "C", hex(i)] for i in range(100000) ])