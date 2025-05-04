def f(x):
    s = ""
    while x != 0:
        s += "0123456789ABCDE"[x % 15]
        x //= 15
    return s[::-1]


dicti = {"0": 0,
         "1": 0,
         "2": 0,
         "3": 0,
         "4": 0,
         "5": 0,
         "6": 0,
         "7": 0,
         "8": 0,
         "9": 0,
         "A": 0,
         "B": 0,
         "C": 0,
         "D": 0,
         "E": 0}

def f1():
    return f(11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338)


for a in f1():
    dicti[a] = f1().count(a)

c = 15
for i in dicti:
    if dicti[i] == 0:
        c -= 1

print(c)

# 10