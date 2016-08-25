m = float(input("Enter weight in pounds: "))
h = float(input("Enter height in inches: "))

m *= 0.45359237
h *= 0.0254

BMI = m / h ** 2

print("BMI is", round(BMI, 4))
