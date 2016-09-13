import turtle, random

NUM = 200
x1, y1 = 0, 0
radius = random.randint(50, NUM)
x2, y2 = random.randint(-NUM, NUM), random.randint(-NUM, NUM)

# Pull the pen down
turtle.circle(radius)
turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(3)
turtle.end_fill()

# Display the status
turtle.penup()

# Pull the pen up
turtle.goto(x1 - 70, y1 - radius - 20)
turtle.pendown()

d = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5

if d <= radius:
    turtle.write("The point is inside the circle")
else:
    turtle.write("The point is outside the circle")
turtle.hideturtle()
turtle.done()
