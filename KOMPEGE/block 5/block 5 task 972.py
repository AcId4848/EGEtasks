for n in range(100, 1000):
    n = str(n)
    s = "".join(sorted([str(int(n[0]) * int(n[1])), str(int(n[1]) * int(n[2]))])[::-1])
    if s == "240":
        print(n)

# 830