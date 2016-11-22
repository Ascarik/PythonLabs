print("{0}{1:>10}{2:>5}{3:>11}{4:>13}".format("Kilograms", "Pounds", "|", "Pounds", "Kilograms"))

pounds = 2.2
pon = 20
for i in range(1, 200, 2):
    print("%d%15.1f%8s%8s%11.2f" % (i,  i* pounds, "|",pon, pon/2.2))
    pon+=5
