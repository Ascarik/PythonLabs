population = 312032486
year = 365

seconds = 5 * year * 24 * 60 * 60

birth = int(seconds / 7)
death = int(seconds / 13)
immigrant = int(seconds / 45)

print("birth:", birth)
print("death:", -death)
print("immigrant:", immigrant)
print("Population projection: ", (birth - death + immigrant))
