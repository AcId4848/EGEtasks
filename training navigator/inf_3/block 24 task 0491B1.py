s = open("0491B1.txt").readline()

s = s.replace("QR", "Q R").replace("RQ", "R Q").replace("RS", "R S").replace("SR", "S R").replace("QS", "Q S").replace("SQ", "S Q")
s = s.replace("QQ", "Q Q").replace("RR", "R R").replace("SS", "S S").replace("QQ", "Q Q").replace("RR", "R R").replace("SS", "S S").split()

print(max([len(i) for i in s]))
# 35
