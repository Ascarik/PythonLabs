import math

amount = eval(input("Loan Amount: "))
years = eval(input("Number of Years: "))

print("Interest Rate   Monthly Payment   Total Payment")
r = 5.0
while r <= 8:
    rate = r / 100
    monthlyPayment = (rate * amount) / (12 * (1 - math.pow(1 + rate / 12, -12 * years)))
    totalPayment = 12 * monthlyPayment * years - amount

    print("%.3f%s          %.3f           %.2f" % (r,"%", monthlyPayment, amount+totalPayment))
    r += 0.125
