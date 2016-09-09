x, y = eval(input("Enter a point's x- and y-coordinates: "))

x1 = 0
y1 = 0

x2 = 0
y2 = 100

x3 = 200
y3 = 0

a = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
b = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
c = 1 - a - b

if a >= 0 and a <= 1 and b >= 0 and b <= 1 and c >= 0 and c <= 1:
    print("The point is in the triangle")
else:
    print("The point is not in the triangle")
