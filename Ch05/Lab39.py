percent = 0
baseSalary = 5000
salesAmount = 30000

result = salesAmount - baseSalary
if result >= 0 and result <= 5000:
    percent = 8
elif result >= 5000.01 and result <= 10000:
    percent = 10
elif result >= 10000.01:
    percent = 12

result = result / (percent/100)
# result = (salesAmount-baseSalary) *

print("the minimum",round(result, 2) , "of sales you have to generate in order to make $",salesAmount)
