def f(x):
    s = ""
    while x != 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]


for N in range(1000):
    R = f(N)
    R = ["1" + R + "02", R + f((N % 3) * 4)][0 if N % 3 == 0 else 1]
    R = int(R, 3)
    if R < 199:
        print(N)

# 20