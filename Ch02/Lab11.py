finalAccountValue = float(input("Enter final account value: "))
interestRate = float(input("Enter annual interest rate in percent: "))
years = float(input("Enter number of years: "))

monthlyInterestRate = interestRate / 12 / 100
numberOfMonths = years * 12

initialDepositAmount = finalAccountValue / ((1 + monthlyInterestRate) ** numberOfMonths)

print("Initial deposit value is", initialDepositAmount)
