year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if month == 1:
    days = 31
    nameday = "January"
elif month == 2:
    if isLeapYear:
        days = 29
    else:
        days = 28
    nameday = "February"
elif month == 3:
    days = 31
    nameday = "March"
elif month == 4:
    days = 30
    nameday = "April"
elif month == 5:
    days = 31
    nameday = "May"
elif month == 6:
    days = 30
    nameday = "June"
elif month == 7:
    days = 31
    nameday = "July"
elif month == 8:
    days = 31
    nameday = "August"
elif month == 9:
    days = 30
    nameday = "September"
elif month == 10:
    days = 31
    nameday = "October"
elif month == 11:
    days = 30
    nameday = "November"
elif month == 12:
    days = 31
    nameday = "December"

print(nameday,year,"has",days,"days")