num = int(input("Enter an integer: "))

print("Is", num, "divisible by 5?", True if num % 5 == 0 else False)
print("Is", num, "divisible by 6?", True if num % 6 == 0 else False)
print("Is", num, "divisible by 5 and 6, but not both?", False if num % 5 == 0 and num % 6 == 0else True)
