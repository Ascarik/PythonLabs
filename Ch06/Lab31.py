import time


def nameDay(nameNumber):
    nameNumber = (4 + nameNumber) % 7
    name = {0: "Вск", 1: "Пон", 2: "Втр", 3: "Срд", 4: "Чтв", 5: "Птн", 6: "Суб", 7: "Вск"}
    return name[nameNumber]


def nameMonth(nameNumber):
    name = {1: "Янв", 2: "Фев",
            3: "Мрт", 4: "Апр",
            5: "Май", 6: "Июн",
            7: "Июл", 8: "Авг",
            9: "Сен", 10: "Окт",
            11: "Ноя", 12: "Дек"
            }
    return name[nameNumber]


def numberYear(numberDay):
    year = 1970
    sum = 0

    while sum < numberDay:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            sum += 366
        else:
            sum += 365
        year += 1

    return year - 1


def numberMonth(numberDay, year):
    month = 0
    y = 1970
    months = [1, 3, 5, 7, 8, 10, 12]
    while y <= year:

        for m in range(1, 13, 1):

            if numberDay <= 31:
                month = m
                break

            if m in months:
                numberDay -= 31
            else:

                if (y % 4 == 0 and y % 100 != 0 and m == 2) or (y % 400 == 0 and m == 2):
                    numberDay -= 29
                elif m == 2:
                    numberDay -= 28
                else:
                    numberDay -= 30

        y += 1
    return "{} {}".format(numberDay + 1, nameMonth(month))


millis = time.time()

tempSeconds = int(millis)
seconds = (int)(tempSeconds % 60);
tempSeconds /= 60  # сколько минут
tempSeconds = int(tempSeconds)
minutes = int(tempSeconds % 60)
tempSeconds /= 60  # сколько часов
hours = int((tempSeconds % 24)) + 3
tempSeconds /= 24  # сколько дней
tempSeconds = int(tempSeconds)
day = int((tempSeconds % 7))

strDay = nameDay(day)
year = numberYear(tempSeconds)

print("{} {}, {}, {}:{}:{}".format(numberMonth(tempSeconds, year), year, strDay, hours, minutes, seconds))
