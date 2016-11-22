max = 0
while True:
    num = eval(input(""))
    if num > max:
        max = num
    if num == 0:
        break;

print("the highest score", max)
