for N in range(1000):
    R = bin(N)[2:]
    R = ["10" + R[2:] + "0", "11" + R[2:] + "1"][sum([int(i) for i in R]) % 2]
    R = int(R, 2)
    if R < 35:
        print(N)

# 24