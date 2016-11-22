step = 1
for i in range(0, 7):

    for q in range(7, 0, -1):
        if q > step:
            print(" ", end=" ")
        else:
            print(q, end=" ")

    for t in range(2, 8):
        if t > step:
            print(" ", end=" ")
        else:
            print(t, end=" ")
    step += 1
    print()
