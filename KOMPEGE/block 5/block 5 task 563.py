for N in range(1, 100):
    R = bin(N)[2:]
    R = R[::-1]
    while R[0] == "0":
        R = R[1:]
    R = int(R, 2)
    if R == 13:
        print(N)

# 88