M = float(input("Enter the amount of water in kilograms: "))
initialTemperature = float(input("Enter the initial temperature: "))
finalTemperature = float(input("Enter the final temperature: "))

Q = M * (finalTemperature - initialTemperature) * 4184

print("The energy needed is", Q)