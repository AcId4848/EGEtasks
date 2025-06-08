from turtle import *

lt(90)
tracer(0)
k = 30
screensize(20000, 20000)

for i in range(2):
    fd(10 * k)
    rt(90)
    fd(20 * k)
    rt(90)

up()

fd(8 * k)
rt(90)
fd(6 * k)
lt(90)

down()

for i in range(2):
    fd(10 * k)
    rt(90)
    fd(7 * k)
    rt(90)

up()

for x in range(20):
    for y in range(19):
        goto(x * k, y * k)
        dot(3)

exitonclick()
# 295