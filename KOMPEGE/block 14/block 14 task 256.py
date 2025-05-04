def f(N, x):
    s = ""
    while N != 0:
        s += "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[N % x]
        N //= x
    return s[::-1]

print([N for N in range(2, 36) if len(f(N, 6)) == 2 and len(f(N, 5)) == 3 and f(N, 11)[-1] == "1"])
# 34
