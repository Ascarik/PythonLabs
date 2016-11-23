import turtle, random, math

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(180)

for i in range(1, 11):
    turtle.penup()
    turtle.goto(0, -100+10*i)
    turtle.pendown()
    turtle.circle(180-10*i)


turtle.done()
