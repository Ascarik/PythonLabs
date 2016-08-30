import math

n = int(input("Enter the number of sides: "))
s = float(input("Enter the side: "))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is", area)
