import turtle


# Draw one chessboard whose upper-left corner is at
# (startx, starty) and bottom-right corner is at (endx, endy)
def drawChessboard(startx, endx, starty, endy):
    turtle.penup()
    turtle.speed(200)

    width = (endx - startx) / 8
    height = (endy - starty) / 8
    if width < 0:
        width *= -1

    if height < 0:
        height *= -1

    flag = True
    print(turtle.heading())
    if int(turtle.heading()) == 45:
        turtle.left(-90)
    else:
        turtle.left(45)
    for i in range(0, 8):

        if i % 2 == 1:
            flag = False
        else:
            flag = True

        for j in range(0, 8):
            turtle.pensize(2)
            turtle.penup()
            turtle.goto(startx + (width + 10) * i, starty - (height + 10) * j)

            turtle.pendown()  # Pull the pen down
            if flag:
                turtle.begin_fill()
                turtle.color("black")
                flag = False
            else:
                flag = True

            turtle.circle(height, steps=4)
            turtle.end_fill()

    turtle.heading()


drawChessboard(-400, -200, 200, 0)
drawChessboard(-100, 100, 200, 0)
turtle.done()
