y = eval(input("Enter a year: "))

isLeapYear = 29 if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else 28
numOfMonth = [31, isLeapYear, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(1, 13):
    year = y
    q = 1

    month = t
    if month < 3:
        month += 12
        year -= 1

    if month < 3:
        month += 12
        year -= 1

    j = year // 100
    k = year % 100

    m = month

    h = (q + ((26 * (m + 1)) / 10) + k + k / 4 + j / 4 + 5 * j) % 7

    h = int(h)

    if h == 0 or h == 1:
        h = 7 - h

    if m == 3:
        nameOfMonth = "March"
    elif m == 4:
        nameOfMonth = "April"
    elif m == 5:
        nameOfMonth = "May"
    elif m == 6:
        nameOfMonth = "June"
    elif m == 7:
        nameOfMonth = "July"
    elif m == 8:
        nameOfMonth = "August"
    elif m == 9:
        nameOfMonth = "September"
    elif m == 10:
        nameOfMonth = "October"
    elif m == 11:
        nameOfMonth = "November"
    elif m == 12:
        nameOfMonth = "December"
    elif m == 13:
        nameOfMonth = "January"
    elif m == 14:
        nameOfMonth = "February"

    flag = False
    step = 1
    shift = 1
    print("%18s %d" % (nameOfMonth, y))
    print("  ===========================")
    print("  Sun Mon Tue Wed Thu Fri Sat")
    while step <= numOfMonth[t - 1]:
        if shift == h or flag:
            print(("%4d" % step), end="")
            flag = True
            step += 1
        else:
            print("    ", end="")

        if shift % 7 == 0:
            print()
        shift += 1

    print("\n\n")
