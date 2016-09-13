import turtle, random

NUM = 200
x1, y1 = random.randint(-NUM, NUM), random.randint(-NUM, NUM)
weight = random.randint(50, NUM * 2)
height = random.randint(50, NUM * 2)

x2 = x1 + weight
y2 = y1 + height

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x1 + weight, y1)
turtle.goto(x1 + weight, y1 + height)
turtle.goto(x1, y1 + height)
turtle.goto(x1, y1)

turtle.penup()
x, y = random.randint(-NUM, NUM), random.randint(-NUM, NUM)
turtle.goto(x, y)
turtle.pendown()
turtle.dot(12, "red")

if x >= x1 and x <= x2 and y >= y1 and y <= y2:
    turtle.write("Point is in the rectangle")
else:
    turtle.write("Point is not in the rectangle")

turtle.done()
