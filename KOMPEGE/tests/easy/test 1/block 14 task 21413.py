def f(x):
    return int(f"82934{x}2", 21) + int(f"2924{x}7", 21) + int(f"67564{x}8", 21)

for x in "0123456789ABCDEFGHIJK":
    if f(x) % 20 == 0:
        print(f(x) // 20)