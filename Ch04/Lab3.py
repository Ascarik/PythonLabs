a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

divisor = a * d - b * c

if divisor == 0:
    print("The equation has no solution")
    quit()

x = (e * d - b * f) / divisor
y = (a * f - e * c) / divisor

print("x is {0:.1f} and y is {1:.1f}".format(x, y))
