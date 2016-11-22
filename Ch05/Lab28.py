import math

E = 1

for i in range(1, 1001):
    E += 1 / math.factorial(i)

print("E =", E)
