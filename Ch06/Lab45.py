import turtle


def drawPolygon(x=0, y=0, radius=50, numberOfSides=3):
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius, steps=numberOfSides)  # Draw a triangle


drawPolygon(-300, 0, 50, 3)
drawPolygon(-200, 0, 50, 4)
drawPolygon(-100, 0, 50, 5)
drawPolygon(0, 0, 50, 6)
drawPolygon(100, 0, 50, 7)
drawPolygon(200, 0, 50, 8)

turtle.done()
