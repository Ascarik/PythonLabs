import math
import turtle


def drawCurvyLine():
    step = 200
    turtle.pensize(4)
    turtle.goto(-step, 0)
    turtle.goto(step, 0)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(0, step)
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(0, -step)
    turtle.penup()
    turtle.goto(step / 2, 0)
    turtle.pendown()
    turtle.write("2\u03c0", font=("Times", 18, "bold"))
    turtle.penup()
    turtle.goto(-step / 2, 0)
    turtle.pendown()
    turtle.write("-2\u03c0", font=("Times", 18, "bold"))

    # -------- sin curly line-------------
    turtle.color("blue")
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(-175, 50 * math.sin((-175 / 100) * 2 * math.pi))
    turtle.pendown()

    for x in range(-175, 176):
        turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))

    # -------- cos curly line-------------
    turtle.color("red")
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(-175, 50 * math.cos((-175 / 100) * 2 * math.pi))
    turtle.pendown()

    for x in range(-175, 176):
        turtle.goto(x, 50 * math.cos((x / 100) * 2 * math.pi))

    # -------- cos curly line-------------
    turtle.color("green")
    turtle.pensize(5)
    turtle.penup()
    scaleFactor = 0.0125
    turtle.goto(-step / 4, scaleFactor * math.pow(step / 4, 2))
    turtle.pendown()

    for x in range(-50, 50):
        turtle.goto(x, scaleFactor * x * x)

    turtle.done()


drawCurvyLine()
