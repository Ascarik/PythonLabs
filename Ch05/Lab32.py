amount = eval(input("Enter an amount: "))

sum = 0
pers = 5 / 100 / 6
for i in range(0, 6):
    sum = (amount + sum) * (1 + pers)

print("sum =", sum)
