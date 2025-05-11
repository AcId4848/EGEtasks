for N in range(100):
    R = bin(N)[2:] + bin(N)[2:][-1]
    R = R + ("0" if R.count("1") % 2 == 0 else "1")
    R = R + ("0" if R.count("1") % 2 == 0 else "1")
    R = int(R, 2)
    if R > 144:
        print(R)

# 156