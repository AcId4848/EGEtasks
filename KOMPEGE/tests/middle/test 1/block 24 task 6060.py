s = open("24_6060.txt").readline()
array = []
for i in range(len(s)-9):
    string = s[i:i+9]
    if string == string[::-1]:
        array.append(string)

print(len(array))