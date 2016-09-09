ta = float(input("Enter the temperature in Fahrenheit between -58 and 41: "))
v = float(input("Enter the wind speed in miles per hour: "))

if ta >= -58 and ta <= 41 and v >= 2:
    twc = 35.74 + 0.6215 * ta - 35.75 * v ** 0.16 + 0.4275 * ta * v ** 0.16
    print("The wind chill index is", round(twc, 5))
else:
    print("Input is invalid")
