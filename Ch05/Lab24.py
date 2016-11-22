import math

loanAmount = eval(input("Loan Amount: "))  # 10000
numberOfYears = eval(input("Number of Years: "))  # 1
annualInterestRate = eval(input("Annual Interest Rate: "))  # 7

rate = annualInterestRate / 100
monthlyPayment = (rate * loanAmount) / (12 * (1 - math.pow(1 + rate / 12, -12 * numberOfYears)))
totalPayment = 12 * monthlyPayment * numberOfYears - loanAmount

monthlyPayment = round(monthlyPayment, 2)

print("Monthly Payment:", monthlyPayment)
print("Total Payment:", round(totalPayment + loanAmount, 2))

n = numberOfYears * 12

print("Payment#\t\tInterest\t\tPrincipal\t\tBalance")
for i in range(1, n + 1):
    r = math.pow(1 + rate / n, n / 12) - 1
    interest = r * loanAmount
    principal = monthlyPayment - interest
    loanAmount = loanAmount - principal

    interest = round(interest, 2)
    principal = round(principal, 2)
    loanAmount = round(loanAmount, 2)
    print(i, "\t\t\t\t", interest, "\t\t\t", principal, "\t\t", loanAmount)
