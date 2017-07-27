import math


def area(n, s):
    return (n * s ** 2) / (4 * math.tan(math.pi / n))


n = int(input("Enter the number of sides: "))
s = float(input("Enter the side: "))

print("The area of the polygon is", area(n, s))
