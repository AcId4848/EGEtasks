def f(x, N):
    s = ""
    while x != 0:
        s += "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[x % N]
        x //= N
    return s[::-1]


print([[f(68, N), N] for N in range(2, 36) if f(68, N)[-1] == "2"])