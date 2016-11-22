num = -1
count = 0
sum = 0
pos = 0
neg = 0
while num != 0:
    num = int(input("Enter an integer, the input ends if it is 0: "))
    sum += num
    count += 1
    if num > 0:
        pos += 1
    elif num < 0:
        neg +=1


print("The number of positives is", (count - pos))
print("The number of negatives is", neg)
print("The total is", count)
print("The average is", (sum / (count-1)))
