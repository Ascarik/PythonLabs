max = 0
premax = 0
while True:
    num = eval(input(""))
    if num > max:
        premax = max
        max = num
    if num == 0:
        break;

print("the highest score", max)
print("second-highest scores", premax)
