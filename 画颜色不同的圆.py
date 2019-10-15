import turtle
import random
t = turtle.Pen()
t.width(3)
t.speed(0)
color_list = ('red', 'yellow', 'green', 'black')
for i in range(10):
    t.penup()
    t.goto(0, -i*10)
    t.pendown()
    t.color(color_list[random.randint(0, 3)])
    t.circle(10+i*10)
turtle.done()
