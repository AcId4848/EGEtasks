s = open("24_8510.txt").readline()

s = s.replace("O", "N").replace("P", "N").replace("NN", "N N").replace("NN", "N N")
s = s.split()
print(s)
print(max(len(x) for x in s))
# 57