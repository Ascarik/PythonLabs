x1, y1, x2, y2, x3, y3 = eval(input("Enter three pofloats for a triangle: "))

# x1, y1, x2, y2, x3, y3 = 1.5, -3.4, 4.6, 5, 9.5, -3.4

x1 = float(x1)
x2 = float(x2)
x3 = float(x3)
y1 = float(y1)
y2 = float(y2)
y3 = float(y3)

side1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
side2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
side3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5

s = (side1 + side2 + side3) / 2

area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

print("The area of the triangle is", round(area, 1))
