num = eval(input("Enter the input integer: "))

i = 2
while i <= num:
    if num % i == 0:
        print(i, end=" ")
        num //= i
    else:
        i += 1
