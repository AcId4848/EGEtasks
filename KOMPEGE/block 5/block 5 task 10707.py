def f(x):
    s = ""
    while x != 0:
        s += str(x % 6)
        x //= 6
    return s[::-1]


for N in range(1, 1000):
    R = f(N)
    R = [R + R[:2], R + f(N % 3 * 10)][0 if N % 3 == 0 else 1]
    R = int(R, 6)
    if R > 680:
        print(R)
        break

# 694
