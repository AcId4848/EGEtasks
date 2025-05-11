for n in range(10, 1000):
    n = str(n)
    arr = [int(n[i] + n[i+1]) for i in range(len(n)-1)]
    R = max(arr) - min(arr)
    if R == 44:
        print(n)
        break

# 159