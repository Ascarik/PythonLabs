import turtle, random


def checkRectangle(x, y, x1, y1, x2, y2, ):
    return x >= x1 and x <= x2 and y >= y1 and y <= y2


NUM = 100
# first rectangle
x1, y1 = random.randint(-NUM, NUM), random.randint(-NUM, NUM)
weight1 = random.randint(50, NUM * 2)
height1 = random.randint(50, NUM * 2)

# x1 = x1 + weight1
# y1 = y1 + height1

turtle.penup()
turtle.color("red")
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x1 + weight1, y1)
turtle.goto(x1 + weight1, y1 + height1)
turtle.goto(x1, y1 + height1)
turtle.goto(x1, y1)

# second rectangle
NUM = NUM // 2
x2, y2 = random.randint(-NUM, NUM), random.randint(-NUM, NUM)
weight2 = random.randint(50, NUM)
height2 = random.randint(50, NUM)

r2x2 = x2 + weight2
r2y2 = y2
r2x3 = x2 + weight2
r2y3 = y2 + height2

r2x4 = x2
r2y4 = y2 + height2

turtle.penup()
turtle.color("blue")
turtle.goto(x2, y2)
turtle.pendown()
turtle.goto(x2 + weight2, y2)
turtle.goto(x2 + weight2, y2 + height2)
turtle.goto(x2, y2 + height2)
turtle.goto(x2, y2)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

if checkRectangle(x2, y2, x1, y1, x1 + weight1, y1 + height1) and \
        checkRectangle(r2x2, r2y2, x1, y1, x1 + weight1, y1 + height1) and \
        checkRectangle(r2x3, r2y3, x1, y1, x1 + weight1, y1 + height1) and \
        checkRectangle(r2x4, r2y4, x1, y1, x1 + weight1, y1 + height1):
    turtle.write("r2 is inside r1")
elif checkRectangle(x2, y2, x1, y1, x1 + weight1, y1 + height1) or \
        checkRectangle(r2x2, r2y2, x1, y1, x1 + weight1, y1 + height1) or \
        checkRectangle(r2x3, r2y3, x1, y1, x1 + weight1, y1 + height1) or \
        checkRectangle(r2x4, r2y4, x1, y1, x1 + weight1, y1 + height1):
    turtle.write("r2 overlaps r1")
else:
    turtle.write("r2 does not overlap r1")

turtle.done()
