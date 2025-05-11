for N in range(1000):
    R = bin(N)[2:] + bin(N)[2:][-1]
    R = R + ("0" if R.count("1") % 2 == 0 else "1")
    R = R + ("0" if R.count("1") % 2 == 0 else "1")
    R = int(R, 2)
    if R > 130:
        print(R, N)

# 17