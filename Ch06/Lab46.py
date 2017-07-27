import turtle


def drawPolygon(x=0, y=0, radius=50):
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius, steps=6)


def drawTriangle(x, y, radius, degree):
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(x, y)
    turtle.right(degree)
    turtle.pendown()
    turtle.circle(radius, steps=3)


def drawCenterLines(radius):
    turtle.penup()
    turtle.goto(0, radius)
    turtle.right(30)

    for i in range(6):
        turtle.pendown()
        turtle.forward(radius)
        turtle.right(60)
        turtle.penup()
        turtle.goto(0, radius)


radius = 100
drawPolygon(0, 0, radius)
drawTriangle(0, 0, radius, 0)
drawTriangle(0, radius * 2, radius, 180)

drawCenterLines(radius)

turtle.done()
