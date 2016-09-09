side1, side2, side3 = eval(input("Enter three edges: "))

if (side1 + side2 > side3) and (side2 + side3 > side1) and \
        (side3 + side1 > side2):
    print("The perimeter is", (side1 + side2 + side3))
else:
    print("The input is invalid")
