deposit = eval(input("Enter the initial deposit amount: "))
percentage = eval(input("Enter annual percentage yield: "))
numberOfMonths = eval(input("Enter maturity period (number of months): "))

numberOfMonths

print("Month  CD Value")
for i in range(1, numberOfMonths + 1):
    deposit = deposit + deposit * percentage / 1200
    print(i, "    ", round(deposit, 2))
