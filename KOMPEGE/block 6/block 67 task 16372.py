from turtle import *
tracer(0)
lt(90)
r = 15
for a in range(2):
    fd(23 * r)
    lt(90)
    bk(27 * r)
    lt(90)
up()
bk(5 * r)
rt(90)
fd(11 * r)
lt(90)
down()
for b in range(2):
    fd(26 * r)
    rt(90)
    fd(32 * r)
    rt(90)

up()
for x in range(44):
    for y in range(-5, 24):
        goto(x * r, y * r)
        dot(3)


print(29 * 44 - 5 * 11 - 2 * 16)
exitonclick()
# 1189