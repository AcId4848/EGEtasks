

for A in range(1000):
    if all((((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & A != 0))) for x in range(10000000)) == 1:
        print(A)
        break