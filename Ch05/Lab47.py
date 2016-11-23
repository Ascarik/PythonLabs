import turtle, random, math

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.pensize(4)
turtle.right(90)
turtle.goto(-100, 100)
turtle.right(90)
turtle.goto(100, 100)
turtle.right(90)
turtle.goto(100, -50)
turtle.right(90)
turtle.goto(-100, -50)

for i in range(0, 100):
    turtle.penup()
    x = random.randint(-100, 100)
    y = random.randint(-50, 100)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(8, "red")


turtle.done()
