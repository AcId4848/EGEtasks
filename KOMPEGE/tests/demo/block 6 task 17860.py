from turtle import *

screensize(20000)
lt(90)
tracer(0)
k = 30
pendown()

for i in range(9):
    fd(22 * k)
    rt(90)
    fd(6 * k)
    rt(90)

penup()

fd(k)
rt(90)
fd(5 * k)
lt(90)

pendown()

for j in range(9):
    fd(53 * k)
    rt(90)
    fd(75 * k)
    rt(90)


up()

for x in range(20):
    for y in range(23):
        goto(x * k, y * k)
        dot(3)


exitonclick()


# 44

