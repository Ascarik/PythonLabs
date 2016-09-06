weight = eval(input("Enter weight in pounds: "))
feet = eval(input("Enter feet: "))
height = eval(input("Enter inches: "))

KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254
FEETS_PER_INCH = 12

weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = (feet * FEETS_PER_INCH + height) * METERS_PER_INCH
bmi = weightInKilograms / (heightInMeters * heightInMeters)


print("BMI is", format(bmi, ".2f"))

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal")
elif bmi < 30:
    print("You are overweight")
else:
    print("You are obese")