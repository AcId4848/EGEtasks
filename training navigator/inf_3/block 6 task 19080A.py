from turtle import *

screensize(2000000, 200000)
tracer(0)
lt(90)
k = 40

rt(315)
for i in range(7):
    fd(16 * k)
    rt(45)
    fd(8 * k)
    rt(135)

up()

for x in range(-11, 1):
    for y in range(20):
        goto(x*k, y*k)
        dot(3)

exitonclick()
# 77
