def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    monthlyInterestRate = monthlyInterestRate / 12 / 100
    numberOfMonths = years * 12

    futureInvestmentValue = investmentAmount * ((1 + monthlyInterestRate) ** numberOfMonths)

    return futureInvestmentValue


print("The amount invested: 1000")
print("Annual interest rate: 9")

print("Years", "Future Value")
for year in range(1, 31):
    print(year, "==", round(futureInvestmentValue(1000, 9, year), 2))
