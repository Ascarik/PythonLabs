def sqrt(n) -> object:
    lastGuess = 1
    while True:
        nextGuess = (lastGuess + (n / lastGuess)) / 2
        checkGuess = nextGuess - lastGuess
        if checkGuess < 0:
            checkGuess *= -1
        if checkGuess < 0.0001:
            return nextGuess
        else:
            lastGuess = nextGuess


print(121, " =", sqrt(121))
print(81, " =", sqrt(81))
print(4589, " =", sqrt(4589))
