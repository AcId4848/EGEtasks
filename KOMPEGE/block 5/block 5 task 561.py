def f(x):
    s = ""
    while x != 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]


for N in range(100):
    R = f(N) + str(N % 3)
    R = int(R, 3)
    print(R)
# 103

