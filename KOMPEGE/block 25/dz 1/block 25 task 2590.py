def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i}
            d |= {x // i}
    return d


for x in range(6080068, 6080176+1):
    d = div(x)
    if len(d) == 2:
        print(x)

# 6080069
# 6080131
# 6080141
# 6080147
# 6080149
# 6080153
# 6080161