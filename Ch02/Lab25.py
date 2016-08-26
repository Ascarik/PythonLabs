import turtle

width = int(input("Enter width: "))
height = int(input("Enter height: "))

turtle.pensize(3)
turtle.penup()
turtle.goto(0, -(height / 2))
turtle.pendown()
turtle.forward(width / 2)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
turtle.forward(width)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
turtle.forward(width / 2)

turtle.done()
