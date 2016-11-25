def displaySortedNumbers(num1, num2, num3):
    if num1 >= num2:
        num1, num2 = num2, num1

    if num2 >= num3:
        num3, num2 = num2, num3

    if num1 >= num3:
        num3, num1 = num1, num3

    return num1, num2, num3


print("The sorted numbers are", displaySortedNumbers(1, 22, 5))
print("The sorted numbers are", displaySortedNumbers(31, 12.4, 15))
