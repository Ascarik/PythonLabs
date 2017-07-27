from math import pow


# Returns true if the sum of any two sides is
# greater than the third side.
def isValid(side1, side2, side3):
    if side1 + side2 < side3:
        return False
    elif side1 + side3 < side2:
        return False
    elif side3 + side2 < side1:
        return False

    return True


# Returns the area of the triangle.
def area(side1, side2, side3):
    s = 0.5 * (side1 + side2 + side3)
    area = pow(s * (s - side1) * (s - side2) * (s - side3), 0.5)
    return area
