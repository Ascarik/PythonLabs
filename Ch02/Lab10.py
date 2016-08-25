v, a = eval(input("Enter speed and acceleration: "))

v = float(v)
a = float(a)
length = v**2 / (2*a)

print("The minimum runway length for this airplane is", round(length, 3), "meters")