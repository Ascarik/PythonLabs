import turtle, random

NUM = 200

x0, y0 = random.randint(-NUM, 0), random.randint(0, NUM)
x1, y1 = random.randint(0, NUM), random.randint(-NUM, 0)
x2, y2 = random.randint(-NUM, NUM), random.randint(-NUM, NUM)
result = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

if result < 0:
    result = "p2 is on the left side of the line from p0 to p1"
elif result > 0:
    result = "p2 is on the right side of the line from p0 to p1"
else:
    result = "p2 is on the same line from p0 to p1"
print(x0, y0)
print(x1, y1)

turtle.pensize(6)
turtle.color("blue")

turtle.penup()
turtle.goto(x0, y0)
turtle.write("P0 ({0}, {1})".format(x0, y0), font=("Times", 18, "bold"))
turtle.pendown()
turtle.goto(x1, y1)
turtle.write("P1 ({0}, {1})".format(x1, y1), font=("Times", 18, "bold"))

turtle.penup()
turtle.color("red")
turtle.goto(x2, y2)
turtle.dot(16, "red")
turtle.write(result, font=("Times", 14, "bold"))
turtle.done()
