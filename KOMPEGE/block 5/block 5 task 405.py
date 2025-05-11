for N in range(100):
    R = bin(N)[2:]
    R = R + ["01", "10"][N % 2]
    R = int(R, 2)
    if R > 81:
        print(R)

# 86