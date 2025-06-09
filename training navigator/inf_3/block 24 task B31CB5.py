s = open("B31CB5.txt").readline()

s = s.replace("KM", "K M").replace("MK", "M K").split()

print(max([len(i) for i in s]))
# 112