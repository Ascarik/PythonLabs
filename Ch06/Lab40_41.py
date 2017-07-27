import turtle
from random import randint


def isPointInsideCircle(xc, xp, yc, yp, radius):
    d = ((xp - xc) ** 2) + ((yp - yc) ** 2)

    if d < radius ** 2:
        return True
    else:
        return False


# Fill a circle
def drawCircle(color="green", x=0, y=0, radius=50):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(radius)

    countCircle = 30
    while countCircle > 0:
        x1 = randint(x - radius, x + radius)
        y1 = randint(y, y + radius * 2)

        if isPointInsideCircle(x, x1, y + radius, y1, radius):
            turtle.penup()
            turtle.goto(x1 - 1, y1 - 1)
            turtle.pendown()
            turtle.begin_fill()
            turtle.color("red")
            turtle.circle(2)
            turtle.end_fill()
            turtle.penup()

            countCircle -= 1


def isPointInsideRectangle(xc, yc, width, height, x, y):
    if not (x >= xc and x <= xc + width):
        return False

    if not (y >= yc and y <= yc + height):
        return False

    return True


# Fill a rectangle
def drawRectangle(color="black", x=0, y=0, width=30, height=30):
    turtle.penup()
    turtle.color(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x + width, y)
    turtle.goto(x + width, y + height)
    turtle.goto(x, y + height)
    turtle.goto(x, y)

    countCircle = 30
    while countCircle > 0:
        x1 = randint(x, x + width)
        y1 = randint(y, y + height)

        if isPointInsideRectangle(x, y, width, height, x1, y1):
            turtle.penup()
            turtle.goto(x1, y1)
            turtle.pendown()
            turtle.begin_fill()
            turtle.color("green")
            turtle.circle(2)
            turtle.end_fill()
            turtle.penup()

            countCircle -= 1


drawCircle("green", 150, 150, 60)
drawRectangle("red", -30, -150, 130, 250)

turtle.done()
