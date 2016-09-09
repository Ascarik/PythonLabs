x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("Enter x1, y1, x2, y2, x3, y3, x4, y4: "))

parallel = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

if parallel == 0:
    print("The two lines are parallel")
else:
    Px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / \
         (parallel)

    Py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / \
         (parallel)
    print("The intersecting point is at ({0:.4f}, {1:.4f})".format(Px, Py))
