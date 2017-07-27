import turtle as turtle
from random import randint


def drawLine(x1, y1, x2, y2, color="green", size=10):
    turtle.penup()
    turtle.color(color)
    turtle.pensize(size)
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.done()


drawLine(0, 0, randint(-100, 300), randint(-100, 300))
