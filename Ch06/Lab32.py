year = eval(input("Enter a year: "))
month = eval(input("Enter a month: "))

isLeapYear = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
numOfMonth = [31, isLeapYear, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

q = 1
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

print("%18s %d" % (nameOfMonth, year), end=" ")
nameOfDays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
print("{} {}".format(nameOfDays[h], 1), end="")
print("\n\n")
