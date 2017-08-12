# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number):
    strNumber = str(number)
    if len(strNumber) == 2:
        return int(strNumber[0]) + int(strNumber[1])
    return number


# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    strNumber = str(number)

    length = len(strNumber)
    sum = 0

    for index in range(length):
        if index % 2 == 0 or index == 0:
            sum += getDigit(int(strNumber[index]) * 2)
    return sum


# Return sum of odd place digits in number
def sumOfOddPlace(number):
    strNumber = str(number)

    length = len(strNumber)
    sum = 0

    for index in range(length):
        if index % 2 == 0 or index == 0:
            sum += getDigit(int(strNumber[length - 1 - index]))
    return sum


# Return true if the card number is valid
def isValid(number):
    evenSum = sumOfDoubleEvenPlace(number)
    oddSum = sumOfOddPlace(number)
    total = evenSum + oddSum
    return total % 10 == 0


if __name__ == '__main__':
    print("Card number1 " + str(4388576018402626) + " is", end=" ")
    print(isValid(4388576018402626))
    print("Card number1 " + str(4388576018410707) + " is", end=" ")
    print(isValid(4388576018410707))
