def format(number, width):
    number = str(number)
    if len(number) > width:
        return number
    else:
        length = len(number)
        for i in range(width - length):
            number = "0" + number

    return number


print(format(34, 5))
print(format(34, 1))
print(format(34, 2))
print(format(34, 3))
