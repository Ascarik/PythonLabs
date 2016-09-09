x2, y2 = eval(input("Enter a point with two coordinates: "))

point_in_circle = (x2**2 + y2**2)**0.5

if point_in_circle <=10:
    result= "is in the circle"
else:
    result = "is not in the circle"


print("Point ({0:.1f}, {1:.1f},) {2}".format(x2, y2, result))