for N in range(1, 10000):
    b = bin(N)[2:]
    k1, k0 = 0, 0
    for i in range(len(b)):
        if (i + 1) % 2 == 0 and b[i] == "1": k1 += 1
        if (i + 1) % 2 != 0 and b[i] == "0": k0 += 1
    R = abs(k1 - k0)
    if R == 5:
        print(N)
        break

# 1023