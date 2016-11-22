import math

summation = 0

for i in range(1, 625):
    summation += 1 / (math.pow(i, 0.5) + math.pow(i + 1, 0.5))

print("summmation =", summation)
