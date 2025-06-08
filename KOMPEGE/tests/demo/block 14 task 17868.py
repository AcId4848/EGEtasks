def f(x):
    return int("98897" + x + "21", 19) + int("2" + x + "923", 19)


for i in "0123456789ABCDEFGH":
    if f(i) % 18 == 0:
        print(f(i) // 18, i)