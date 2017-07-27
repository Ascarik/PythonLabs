import math


def area(s):
    return (5 * s ** 2) / (4 * math.tan(math.pi / 5))


s = float(input("Enter the side: "))

print("The area of the pentagon is", area(s))
