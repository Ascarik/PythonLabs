
def computeCommission(salesAmount):
    if salesAmount >= 0 and salesAmount <= 5000:
        percent = 8
    elif salesAmount >= 5000.01 and salesAmount <= 10000:
        percent = 10
    elif salesAmount >= 10000.01:
        percent = 12

    return salesAmount * (percent / 100)

print(
    format("Sales Amount", "20s"), format("Commission", ">10s"),end="\n\n"
)


for salesAmount in range(10000, 105000, 5000):
    print(format(salesAmount, "<20.1f"), format(computeCommission(salesAmount), ">10.2f"))

