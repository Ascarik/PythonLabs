minutes = int(input("Enter the number of minutes: "))

days = minutes // 60
days //= 24
years = days // 365
days %= 365

print(minutes, "minutes is approximately", years, "years and", days, "days")
