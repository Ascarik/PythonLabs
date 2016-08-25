year = int(input("Enter the number of years: "))
population = 312032486
day = 365

seconds = year * day * 24 * 60 * 60

birth = int(seconds / 7)
death = int(seconds / 13)
immigrant = int(seconds / 45)

print("The population in {0} years is {1}".format(year, (population + birth - death + immigrant)))
