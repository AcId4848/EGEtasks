for N in range(10000):
    R = bin(N)[2:]
    R = R + str(sum([int(d) for d in R]) % 2)
    R = R + str(sum([int(d) for d in R]) % 2)
    R = int(R, 2)
    if R > 80:
        print(R)
        break

# 86