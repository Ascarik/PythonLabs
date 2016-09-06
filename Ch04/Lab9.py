weight1, price1 = eval(input("Enter weight and price for package 1: "))
weight2, price2 = eval(input("Enter weight and price for package 2: "))

num = 1

if weight1 / price1 < weight2 / price2:
    num = 2

print("Package", num, "has the better price.")
