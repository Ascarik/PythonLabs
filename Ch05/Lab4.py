print("{0} {1:>20}".format("Miles", "Kilometers"))
conKil = 1.609

for i in range(1, 11):
    if i < 10:
        print("{0} {1:>25.3f}".format(i, i * conKil))
    else:
        print("{0} {1:>24.3f}".format(i, i * conKil))
