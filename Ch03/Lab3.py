import math

# Atlanta, Georgia  -84.3879824 , 33.7489954
# Orlando, Florida  -81.37923649999999 , 28.5383355
# Savannah, Georgia  -81.09983419999998 , 32.0835407
# Charlotte, North Carolina -80.84312669999997 , 35.2270869

x1, y1 = -84.3879824 , 33.7489954
x2, y2 = -81.37923649999999 , 28.5383355
x3, y3 = -81.09983419999998 , 32.0835407
x4, y4 = -80.84312669999997 , 35.2270869

radius = 6371.01

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

area1 = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5


x1 = float(x1)
x2 = float(x3)
x3 = float(x4)
y1 = float(y1)
y2 = float(y3)
y3 = float(y4)

side1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
side2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
side3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5

s = (side1 + side2 + side3) / 2

area2 = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5


area = area1 + area2

print("the area of a polygon is",area)