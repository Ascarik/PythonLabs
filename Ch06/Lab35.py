from random import randint  # import randint


# Generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))


# Generate a random uppercase letter
def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')


def getQuantity(ch):
    count = 0
    for i in range(10000):
        ch = getRandomUpperCaseLetter()
        if ch == "A":
            count += 1
    return count


print("The quantity A is {}".format(getQuantity("A")))
