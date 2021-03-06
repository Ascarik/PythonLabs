def generetePalindromicNumbers(numberOfPrimes):
    NUMBER_OF_PRIMES_PER_LINE = 10
    countPrint = 0
    number = 2
    count = 1

    while count <= numberOfPrimes:

        isPrime = True
        divisor = 2

        while divisor <= number // 2:
            if number % divisor == 0:
                isPrime = False
                break
            divisor += 1

        if isPrime:
            if number == int(str(number)[::-1]):
                count = count + 1
                countPrint += 1
                print(format(number, "10d"), end='')
                if countPrint % NUMBER_OF_PRIMES_PER_LINE == 0:
                    print()

        number += 1


generetePalindromicNumbers(100)
