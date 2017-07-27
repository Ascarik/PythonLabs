def isExistPrime(number) -> bool:
    divisor = 2
    while divisor <= number // 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def generateTwinPrimeNumbers(numberOfPrimes):
    number = 2
    count = 1

    while number <= numberOfPrimes:

        isPrime = True
        divisor = 2

        while divisor <= number // 2:
            if number % divisor == 0:
                isPrime = False
                break
            divisor += 1

        if isPrime:
            if isExistPrime(number + 2):
                count = count + 1
                print("({} {})".format(number, number + 2))

        number += 1


generateTwinPrimeNumbers(1000)
