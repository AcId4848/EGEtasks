for i in range(81234, 134690):
    de = [d for d in range(2, i-1) if i % d == 0]
    if len(de) == 3:
        print(i, de)

# 83521 [17, 289, 4913]
# 130321 [19, 361, 6859]