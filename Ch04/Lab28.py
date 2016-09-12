def checkRectangle(x, y, x1, y1, x2, y2, ):
    return x >= x1 and x <= x2 and y >= y1 and y <= y2


x1, y1, weight1, height1 = eval(input("Enter r1's center x-, y-coordinates, width, and height: "))
x2, y2, weight2, height2 = eval(input("Enter r2's center x-, y-coordinates, width, and height: "))

# the points for the first rectangle
r1x1 = x1 - weight1 / 2
r1y1 = y1 - height1 / 2

r1x2 = x1 + weight1 / 2
r1y2 = y1 + height1 / 2

# the points for the second rectangle
r2x1 = x2 - weight2 / 2
r2y1 = y2 - height2 / 2

r2x2 = x2 + weight2 / 2
r2y2 = y2 - height2 / 2

r2x3 = x2 + weight2 / 2
r2y3 = y2 + height2 / 2

r2x4 = x2 - weight2 / 2
r2y4 = y2 + height2 / 2

if checkRectangle(r2x1, r2y1, r1x1, r1y1, r1x2, r1y2) and \
        checkRectangle(r2x2, r2y2, r1x1, r1y1, r1x2, r1y2) and \
        checkRectangle(r2x3, r2y3, r1x1, r1y1, r1x2, r1y2) and \
        checkRectangle(r2x4, r2y4, r1x1, r1y1, r1x2, r1y2):
    print("r2 is inside r1")
elif checkRectangle(r2x1, r2y1, r1x1, r1y1, r1x2, r1y2) or \
        checkRectangle(r2x2, r2y2, r1x1, r1y1, r1x2, r1y2) or \
        checkRectangle(r2x3, r2y3, r1x1, r1y1, r1x2, r1y2) or \
        checkRectangle(r2x4, r2y4, r1x1, r1y1, r1x2, r1y2):
    print("r2 overlaps r1")
else:
    print("r2 does not overlap r1")
