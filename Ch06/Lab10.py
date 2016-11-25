# Check whether number is prime
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False  # number is not a prime
        divisor += 1
    return True  # number is prime


def findPrimeNumber(toTillNumber):
    count = 2
    primeNumber = 0


    while count < toTillNumber:
        # Print the prime number and increase the count
        if isPrime(count):
            primeNumber = count
        count += 1

    return primeNumber

print(findPrimeNumber(10000))

