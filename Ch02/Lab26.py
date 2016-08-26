import turtle

radius = int(input("Enter radius: "))
PI = 3.14

area = PI * radius**2

turtle.pensize(3)
turtle.circle(radius)
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.write(area)

turtle.done()
