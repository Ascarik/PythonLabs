print("{0}{1:>16}{2:>3}{3:>16}{4:>13}".format("Miles", "Kilometers", "|", "Kilometers", "Miles"))

kilometers = 1.609
kil = 20
for i in range(1, 200, 2):
    print("%d%15.3f%8s%8s%16.3f" % (i, i * kilometers, "|", kil, kil / 1.609))
    kil += 5
