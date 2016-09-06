# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display the results
print("Your amount", amount, "consists of\n",
      ("\t" + str(numberOfOneDollars) + " dollars\n") if numberOfOneDollars != 0 else "",
      ("\t" + str(numberOfQuarters) + " quarters\n") if numberOfQuarters != 0 else "",
      ("\t" + str(numberOfDimes) + " dimes\n") if numberOfDimes != 0 else "",
      ("\t" + str(numberOfNickels) + " nickels\n") if numberOfNickels != 0 else "",
      ("\t" + str(numberOfPennies) + " pennies") if numberOfPennies != 0 else "",
      end="")
