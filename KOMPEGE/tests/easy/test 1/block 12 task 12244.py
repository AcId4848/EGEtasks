for n in range(3, 10001):
    s = "3" + n * "5"
    while "333" in s or "555" in s:
        if "555" in s:
            s = s.replace("555", "3", 1)
            s = s.replace("333", "5", 1)
    print(s)
