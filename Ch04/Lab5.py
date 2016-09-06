def dayOfWeek(todayDay):
    if todayDay == 1:
        name_day = "Monday"
    elif todayDay == 2:
        name_day = "Tuesday"
    elif todayDay == 3:
        name_day = "Wednesday"
    elif todayDay == 4:
        name_day = "Thursday"
    elif todayDay == 5:
        name_day = "Friday"
    elif todayDay == 6:
        name_day = "Saturday"
    elif todayDay == 0:
        name_day = "Sunday"
    return name_day


todayDay = int(input("Enter today's day: "))
futureDay = int(input("Enter the number of days elapsed since today: "))

nameTodayDay = dayOfWeek(todayDay)
if futureDay <= 6:
    futureDay += todayDay
else:
    futureDay = (todayDay + futureDay) % 7

nameFutureDay = dayOfWeek(futureDay)

print("Today is {0} and the future day is {1}".format(nameTodayDay, nameFutureDay))
