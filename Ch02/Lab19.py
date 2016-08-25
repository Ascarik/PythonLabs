investmentAmount = float(input("Enter final account value: "))
interestRate = float(input("Enter annual interest rate: "))
years = float(input("Enter number of years: "))

monthlyInterestRate = interestRate / 12 / 100
numberOfMonths = years * 12

futureInvestmentValue = investmentAmount * ((1 + monthlyInterestRate) ** numberOfMonths)

print("Accumulated value is", round(futureInvestmentValue, 2))
