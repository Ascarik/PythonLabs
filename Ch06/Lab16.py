def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def getTotalDaysInYear(year):
    if isLeapYear(year):
        return 366
    else:
        return 365


for year in range(2000, 2020):
    print(year, "has", getTotalDaysInYear(year), "days")
