import turtle, random, math

turtle.penup()
turtle.goto(-150, 100)
turtle.write("Multiplication Table", font=("Times", 18, "bold"))

for i in range(1, 10):
    turtle.penup()
    turtle.goto(-170, 100 - 25 * i)

    if i > 1:
        turtle.write(str(i) + " |  ", font=("Times", 12, "bold"))
    else:
        if i > 1:
            turtle.write(str(i), font=("Times", 12, "bold"))

    for j in range(2, 10):
        if i == 1:
            turtle.penup()
            turtle.goto(-170, 100 - 40 * i)
            turtle.write("------------------------------------", font=("Times", 18, "bold"))

        turtle.penup()
        turtle.goto(-170 + 30 * j, 100 - 25 * i)
        turtle.write(str(i * j) + "  ", font=("Times", 12, "bold"))

turtle.done()
