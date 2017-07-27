# Return true if point (x2, y2) is on the left side of the
# directed line from (x0, y0) to (x1, y1)
def leftOfTheLine(x0, y0, x1, y1, x2, y2):
    result = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

    if result > 0:
        return True

    return False


# Return true if point (x2, y2) is on the same
# line from (x0, y0) to (x1, y1)
def onTheSameLine(x0, y0, x1, y1, x2, y2):
    result = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

    if result == 0:
        return True

    return False


# Return true if point (x2, y2) is on the
# line segment from (x0, y0) to (x1, y1)
def onTheLineSegment(x0, y0, x1, y1, x2, y2):
    result = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

    return (result <= 0) and (((x0 <= x2) and (x2 <= x1)) or ((x0 >= x2) and (x2 >= x1)))


x0, y0, x1, y1, x2, y2, = eval(input("Enter coordinates for the three points p0, p1, and p2: "))

if leftOfTheLine(x0, y0, x1, y1, x2, y2) > 0:
    print("p2 is on the left side of the line from p0 to p1")

if onTheSameLine(x0, y0, x1, y1, x2, y2):
    print("p2 is on the same line from p0 to p1")

if onTheSameLine(x0, y0, x1, y1, x2, y2):
    print("p3 is line segment from p0 to p1")
