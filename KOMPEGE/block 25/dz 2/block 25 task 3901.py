from fnmatch import fnmatch


for x in range(700000, 1000000):
    if x % 13 == 0 and not fnmatch(str(x), "*0??3*") and not fnmatch(str(x), "*4??2") and not fnmatch(str(x), "*1*"):
        print(x, sum([int(i) for i in str(x)]))

# 700024 13
# 700050 12
# 700076 20
# 700089 24
# 700206 15