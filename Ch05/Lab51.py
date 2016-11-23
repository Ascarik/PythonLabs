import turtle

step = 180
turtle.penup()
turtle.goto(-step, step)

for i in range(0, 19):
    turtle.penup()
    turtle.goto(-step, step - 10 * i)
    turtle.pendown()
    turtle.goto(0, step - 10 * i)

    turtle.penup()
    turtle.goto(-step + 10 * i, step)
    turtle.pendown()
    turtle.goto(-step + 10 * i , 0)

turtle.done()
