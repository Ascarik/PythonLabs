import Ch06.MyTriangle

s1, s2, s3 = eval(input("Enter three sides in double:"))

if Ch06.MyTriangle.isValid(s1, s2, s3):
    print("The area of the triangle is", Ch06.MyTriangle.area(s1, s2, s3))
else:
    print("Input is invalid")
