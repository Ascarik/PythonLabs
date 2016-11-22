import math
print("Degree Sin Cos")

for i in range(0,361,10):
    print("{0}   {1:.4f}   {2:.4f}".format(i, math.sin(math.radians(i)), math.cos(math.radians(i))))