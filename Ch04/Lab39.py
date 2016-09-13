import turtle, random, math

radius1 = random.randint(50, 150)
x1, y1 = 0, radius1 // 2
turtle.color("red")
turtle.pensize(4)
turtle.penup()
turtle.pendown()
turtle.circle(radius1)

x2, y2 = random.randint(-radius1, radius1), random.randint(-radius1, radius1)
radius2 = random.randint(10, 50)
turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.color("blue")
turtle.circle(radius2)

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

if distance <= math.fabs(radius1 - radius2):
    turtle.write("circle2 is inside circle1")
elif distance <= math.fabs(radius1 + radius2):
    turtle.write("circle2 overlaps circle1")
else:
    turtle.write("circle2 does not overlap circle1")

turtle.done()
