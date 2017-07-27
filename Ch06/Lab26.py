def printMersenneNumners(number):
    for i in range(number):
        i += 1
        print("{:>5} {:>20}".format(i, 2 ** i - 1))


printMersenneNumners(31)
