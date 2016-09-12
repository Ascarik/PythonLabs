x0, y0, x1, y1, x2, y2, = eval(input("Enter coordinates for the three points p0, p1, and p2: "))

result = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

if result > 0:
    print("p2 is on the left side of the line from p0 to p1")
elif result < 0:
    print("p2 is on the right side of the line from p0 to p1")
else:
    print("p2 is on the same linefrom p0 to p1")
