import random
from math import sqrt

a = []
sumForMean = 0
sumForDeviation = 0

for i in range(0, 10):
    d = random.random() * 100
    a.append(d)
    d = a[i]
    print("number", d)
    sumForMean += d
    sumForDeviation += d * d

deviation = sqrt((sumForDeviation - sumForMean * sumForMean / len(a)) / (len(a) - 1))

mean = sumForMean / len(a)

print("The mean is", mean)
print("The standard deviation is", deviation)
