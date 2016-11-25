def printChars(ch1, ch2, numberPerLine):
    for i in range(numberPerLine):
        for j in range(ord(ch1), ord(ch2)+1):
            print(chr(j), sep=" ", end="")
        print()


printChars('A','z', 10)
