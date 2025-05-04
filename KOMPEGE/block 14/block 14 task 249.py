for x in range(1000):
    if str(x).count("3") + str(x).count("4") + str(x).count("5") + str(x).count("6") + str(x).count("7") + str(x).count("8") + str(x).count("9") == 0:
        if 20 < int(str(x), 3) < 30:
            if "11" in str(x):
                print(int(str(x), 3))

# 22
