import math

sum = 0
number = 2
while True:
    isPrime = True
    divisor = 2

    while divisor <= number / 2:
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1


    if isPrime:
        sum = math.pow(2, number - 1) * (math.pow(2, number) - 1)

        if sum > 10000:
            break
        print("Perfect number is", sum)

    number += 1
