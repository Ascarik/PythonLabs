hexnum = input("Enter a hex character:")

if hexnum >= '0' and hexnum <= '9' or hexnum >= 'A' and hexnum <= 'F':
    if hexnum >= '0' and hexnum <= '9':
        print("The decimal value is", int(hexnum))
    else:
        print("The hex value is", ord(hexnum) - 55)
