from fnmatch import fnmatch

def count(x):
    c = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            if i % 2 == 0:
                c.append(i)
            if x // i % 2 == 0:
                c.append(x // i)
    return c

for x in range(65001, 1000000):
    if fnmatch(str(x), "6*97*5?") and len(count(x)) >= 4:
        print(x, sum(count(x)))

# 69750 129792
# 69752 122080
# 69756 139536
# 69758 75152
# 609750 1103232
# 609752 1291248
# 609754 630840