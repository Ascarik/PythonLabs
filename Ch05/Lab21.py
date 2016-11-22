step = 1
for i in range(0, 8):

    count = 1

    for q in range(0, 8):
        if q < 8 - step:
            print("    ", end="")
        else:
            # print(count, end="  ")
            print("{0:4}".format(count), end="")
            count *= 2

    count //= 4

    for t in range(0, 7):
        if count == 0:
            print("    ", end="")
        else:
            print("{0:4}".format(count), end="")
            count //= 2

    step += 1
    print()
