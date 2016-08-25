savingAmount = float(input("Enter the monthly saving amount: "))
percent = float(input("Enter interest rate: "))
percent /= 100 * 12
# percent /= 12

sum = 0
for i in range(1, 7):
    sum = (savingAmount + sum) * (1 + percent)

print("After the sixth month, the account value is", round(sum, 2))
