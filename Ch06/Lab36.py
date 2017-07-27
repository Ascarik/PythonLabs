from random import randint  # import randint


# Generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))


# Generate a random uppercase letter
def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')


def getRandomNumbers():
    return getRandomCharacter('0', '9')


def generateSymbols():
    for i in range(1, 201):
        if i <= 100:
            print("{:>4}".format(getRandomUpperCaseLetter()), end="")
        else:
            print("{:>4}".format(getRandomNumbers()), end="")

        if i % 10 == 0:
            print()


generateSymbols()
