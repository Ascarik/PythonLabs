def displayPattern(n):
    for i in range(n + 1):
        for j in range(n, 0, -1):
            if (i >= j):
                print(j, end="  ")
            else:
                print(" ", end="  ")
        print()


displayPattern(9)
