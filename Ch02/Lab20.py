balance, annualInterestRate = eval(input("Enter balance and interest rate (e.g., 3 for 3%): "))

balance = float(balance)
annualInterestRate = float(annualInterestRate)

# annualInterestRate /= 100

interest = balance * (annualInterestRate / 1200 )

print("The interest is",round(interest, 5))

