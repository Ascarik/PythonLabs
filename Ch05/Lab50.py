import turtle

turtle.penup()
turtle.goto(-150, 100)

count = 1
while True:

    for j in range(0, count):
        turtle.penup()
        turtle.goto(-150 + 30 * j, 100 - 25 * count)
        turtle.write(str(j + 1) + "  ", font=("Times", 18, "bold"))

    count += 1

    if count > 10:
        break

turtle.done()
