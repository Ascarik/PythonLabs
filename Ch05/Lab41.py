step = 0
count = 0
imax = 0
num = 0
while (step < 7):
    if imax == 0:
        imax = int(input("Enter a number (0: for end of input): "))
    else:
        num = int(input("Enter a number (0: for end of input): "))

    if imax == num:
        count += 1
    elif imax < num:
        imax = num
        count = 1
    step += 1

print("The largest number is", imax)
print("The occurrence count of the largest number is", count)
