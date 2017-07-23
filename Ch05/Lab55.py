import turtle

flag = True
turtle.left(45)
for i in range(0, 8):

    if i % 2 == 1:
        flag = False
    else:
        flag = True

    for j in range(0, 8):
        turtle.pensize(3)
        turtle.penup()
        turtle.goto(-200 + 60 * j, 150 - 60 * i)

        turtle.pendown()  # Pull the pen down
        if flag:
            turtle.begin_fill()
            turtle.color("black")
            flag = False
        else:
            flag = True

        turtle.circle(40, steps=4)
        turtle.end_fill()

turtle.done()
