y = int(input("Enter year: (e.g., 2008): "))

for t in range(1, 13):
    year = y
    q = 1

    month = t
    if month < 3:
        month += 12
        year -= 1

    j = year // 100
    k = year % 100

    m = month

    h = (q + ((26 * (m + 1)) / 10) + k + k / 4 + j / 4 + 5 * j) % 7

    h = round(h)

    if h == 0:
        dayOfWeek = "Saturday"
    elif h == 1:
        dayOfWeek = "Sunday"
    elif h == 2:
        dayOfWeek = "Monday"
    elif h == 3:
        dayOfWeek = "Tuesday"
    elif h == 4:
        dayOfWeek = "Wednesday"
    elif h == 5:
        dayOfWeek = "Thursday"
    elif h == 6:
        dayOfWeek = "Friday"

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


    print(nameOfMonth, 1,",", y, "is",dayOfWeek)
