hexnum = eval(input("Enter a decimal value (0 to 15):"))

if hexnum >= 0 and hexnum <= 15:
    if hexnum < 10:
        print("The hex value is", hexnum)
    else:
        print("The hex value is", chr(55 + hexnum))
