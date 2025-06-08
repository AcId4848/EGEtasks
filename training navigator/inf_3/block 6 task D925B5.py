from turtle import *

screensize(2500, 2500)
tracer(0)
lt(90)
k = 20

for i in range(2):
    fd(3 * k)
    lt(90)
    bk(10 * k)
    lt(90)

up()

bk(10 * k)
rt(90)
fd(9 * k)
lt(90)

down()

for i in range(2):
    fd(16 * k)
    rt(90)
    fd(8 * k)
    rt(90)

up()

for x in range(18):
    for y in range(-10, 7):
        goto(x * k, y * k)
        dot(3)

exitonclick()

# 189