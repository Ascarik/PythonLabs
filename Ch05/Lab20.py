count = 1
for i in range(0, 6):

    for q in range(1, 7):
        if q > count:
            print(" ", end=" ")
        else:
            print(q, end=" ")

    print("  ", end="")
    revcount = 7 - count
    for q in range(1, 7):
        if q > revcount:
            print(" ", end=" ")
        else:
            print(q, end=" ")

    print("  ", end="")
    for q in range(6, 0, -1):
        if q > count:
            print(" ", end=" ")
        else:
            print(q, end=" ")

    print("  ", end="")
    for q in range(1, 7):
        if q < count:
            print(" ", end=" ")
        else:
            print(q, end=" ")

    count += 1
    print()
