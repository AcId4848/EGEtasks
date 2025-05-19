for n in range(255):
    R = "0" * (8 - len(f"{n:b}")) + f"{n:b}"
    R = R[:2] + R[6:]
    if int(R, 2) == 7:
        print(n, R, int(R, 2))

# 107