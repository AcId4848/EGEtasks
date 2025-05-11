for n in range(100, 1000):
    n = str(n)
    s = "".join(sorted([str(int(n[0]) ** 2 + int(n[1]) ** 2), str(int(n[1]) ** 2 + int(n[2]) ** 2)])[::-1])
    if s == "9010":
        print(n)

# 139