for n in range(1000, 10000):
    n = str(n)
    s = "".join(sorted([str(int(n[0]) * int(n[1])), str(int(n[2]) * int(n[3]))]))
    if s == "1214":
        print(sorted([str(int(n[0]) * int(n[1])), str(int(n[2]) * int(n[3]))]))
        print(n)

# 7262