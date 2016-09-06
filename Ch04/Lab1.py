a, b, c = eval(input("Enter a, b, c:"))

discriminant = b ** 2 - 4 * a * c

if discriminant < 0:
    print("The equation has no real roots")
    quit()

x1 = (-b + discriminant ** 0.5) / (2 * a)

if discriminant == 0:
    print("The root is", x1)
    quit()

x2 = (-b - discriminant ** 0.5) / (2 * a)

print("The roots are {0:.5f} and {1:.5f}".format(x1, x2))
