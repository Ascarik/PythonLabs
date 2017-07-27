import turtle
from random import randint  # import randint


# Generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))


def getRandomLowerCaseLetter():
    return getRandomCharacter('a', 'z')


def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')


def getRandomNumbers():
    return getRandomCharacter('0', '9')


def printSymbols():
    turtle.penup()
    turtle.goto(-150, 100)

    j = 0
    i = 0
    count = 0
    while count <= 100:
        choice = randint(1, 100)
        for j in range(0, 15):
            choice = randint(1, 100)
            if choice <= 33:
                sym = getRandomUpperCaseLetter()
            elif choice <= 66:
                sym = getRandomLowerCaseLetter()
            else:
                sym = getRandomNumbers()

            turtle.penup()
            turtle.goto(-150 + 30 * j, 100 - 25 * i)
            turtle.write(sym + "  ", font=("Times", 18, "bold"))

        i += 1
        count += 15

    turtle.done()


printSymbols()
