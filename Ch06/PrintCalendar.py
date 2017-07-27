# Get the English name for the month
from Ch06.ShowCurrentTime import getCurrentTime


def getMonthName(month):
    if month == 1:
        monthName = "January"
    elif month == 2:
        monthName = "February"
    elif month == 3:
        monthName = "March"
    elif month == 4:
        monthName = "April"
    elif month == 5:
        monthName = "May"
    elif month == 6:
        monthName = "June"
    elif month == 7:
        monthName = "July"
    elif month == 8:
        monthName = "August"
    elif month == 9:
        monthName = "September"
    elif month == 10:
        monthName = "October"
    elif month == 11:
        monthName = "November"
    else:
        monthName = "December"

    return monthName


# Get the start day of month/1/year
def getStartDay(year, month):
    START_DAY_FOR_JAN_1_1800 = 3

    # Get total number of days from 1/1/1800 to month/1/year
    totalNumberOfDays = getTotalNumberOfDays(year, month)

    # Return the start day for month/1/year
    return (totalNumberOfDays + START_DAY_FOR_JAN_1_1800) % 7


# Get the total number of days since January 1, 1800
def getTotalNumberOfDays(year, month):
    total = 0

    # Get the total days from 1800 to 1/1/year
    for i in range(1800, year):
        if isLeapYear(i):
            total = total + 366
        else:
            total = total + 365

    # Add days from Jan to the month prior to the calendar month
    for i in range(1, month):
        total = total + getNumberOfDaysInMonth(year, i)

    return total


# Get the number of days in a month
def getNumberOfDaysInMonth(year, month):
    if (month == 1 or month == 3 or month == 5 or month == 7 or
                month == 8 or month == 10 or month == 12):
        return 31

    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30

    if month == 2:
        return 29 if isLeapYear(year) else 28

    return 0  # If month is incorrect


# Determine if it is a leap year
def isLeapYear(year) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def getDayName(day, month, year):
    days = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]

    if day > 28 and month == 2 \
            or day > 31 \
            or day < 1 \
            or month > 12 \
            or month < 1:
        print("Invalid date")

    if month < 3:
        month += 12
        year -= 1

    j = year // 100
    k = year % 100
    m = month
    h = (day + ((26 * (m + 1)) / 10) + k + k / 4 + j / 4 - 2 * j) % 7
    h = int(h)

    print(h)
    return days[h]


def getCurrentDate():
    # Prompt the user to enter year and month
    year = eval(input("Enter full year (e.g., 2001): "))
    month = eval(input("Enter month as number between 1 and 12: "))
    day = eval(input("Enter day as number between 1 and 31: "))

    dayName = getDayName(day, month, year)

    print("{}/{}/{} {} {}".format(day, month, year, dayName, getCurrentTime()))
