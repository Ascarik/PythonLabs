x0, y0, x1, y1, x2, y2, = eval(input("Enter coordinates for the three points p0, p1, and p2: "))

result = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
print(result)

if result == 0:
    print("({0}, {1}) is on the line segment from ({2}, {3}) to ({4}, {5})".format(x2, y2, x0, y0, x1, y1))
else:
    print("({0}, {1}) is not on the line segment from ({2}, {3}) to ({4}, {5})".format(x2, y2, x0, y0, x1, y1))
