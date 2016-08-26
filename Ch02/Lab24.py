import turtle

turtle.pensize(3)
turtle.goto(0, 0)
turtle.circle(30, steps=6)
turtle.penup()
turtle.goto(0, -60)
turtle.pendown()
turtle.circle(30, steps=6)
turtle.penup()
turtle.goto(-60, 0)
turtle.pendown()
turtle.circle(30, steps=6)
turtle.penup()
turtle.goto(-60, -60)
turtle.pendown()
turtle.circle(30, steps=6)

turtle.done()
