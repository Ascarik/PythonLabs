import math

PI = 0

for i in range(1, 100000 + 1):
    PI += math.pow(-1, i + 1) / (2 * i - 1)

PI *= 4
print("PI =", PI)
