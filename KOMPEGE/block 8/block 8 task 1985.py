from itertools import permutations

array = []
glas = ["АИ", "АО", "АУ", "ИА", "ИО", "ИУ", "ОА", "ОИ", "ОУ", "УА", "УИ", "УО"]
sogl = ["БК", "БЛ", "БН", "КБ", "КЛ", "КН", "ЛБ", "ЛК", "ЛН", "НБ", "НК", "НЛ"]
for a in permutations("АБИКОЛУН"):
    a = "".join(a)
    if [1 for t in glas if t not in a] == [1 for i in range(12)] and [1 for t in sogl if t not in a] == [1 for i in range(12)]:
        array.append(a)

print(len(array))
# 1152