import random

num1 = random.randint(0, 99)
num2 = random.randint(0, 99)
num3 = random.randint(0, 99)

if num1 > num3:
    num1, num3 = num3, num1
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2

print(num1, num2, num3)
