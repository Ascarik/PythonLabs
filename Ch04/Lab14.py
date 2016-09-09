import random

coin = random.randint(0, 1)
user_choose = int(input("Enter a coin(0 or 1): "))

print("the guess is", True if coin == user_choose else False)