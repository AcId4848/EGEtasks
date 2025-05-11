for N in range(10000):
    R = bin(2 * N)[2:]
    R = R + str(sum([int(i) for i in R]) % 2)
    R = R + str(sum([int(i) for i in R]) % 2)
    R = int(R, 2)
    if R > 1017:
        print(N)
        break

# 127