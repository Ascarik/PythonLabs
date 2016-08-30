import turtle


turtle.penup()
turtle.goto(0, -100)
turtle.left(30)
turtle.pendown()
turtle.color("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(150, steps = 6)
turtle.end_fill()
turtle.goto(-140,0)
turtle.color("white")
turtle.write("STOP", font=("Arial", 45, "bold"))
turtle.done()