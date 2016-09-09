x2,y2 = eval(input("Enter a point with two coordinates: "))

width = 10
height = 5

if x2 <= width/2 and y2<=height/2:
    print("Point is in the rectangle")
else:
    print("Point is not in the rectangle")