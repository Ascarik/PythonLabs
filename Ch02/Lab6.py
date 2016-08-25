number = int(input("Enter a number between 0 and 1000: "))

num1 = number % 10
number //= 10
num2 = number % 10
number //= 10
num3 = number

print("The sum of the digits is", num1 + num2 + num3)
