for i in range(250200, 1000000):
    de = [d for d in range(2, i-1) if i % d == 0]
    if len(de) == 0:
        de = [0]
    if (max(de) + min(de)) % 123 == 17:
        print(i, max(de) + min(de))

# 250212 125108
# 250458 125231
# 250593 83534
# 250621 35810
# 250704 125354
