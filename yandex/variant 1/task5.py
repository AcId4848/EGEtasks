for N in range(10000):
    R = bin(N)[2:]
    R = R + str(R.count("1") % 2)
    R = R + str(R.count("1") % 2)
    if int(R, 2) > 198:
        print(int(R, 2))
        break
