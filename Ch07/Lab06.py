class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminant(self):
        return self.__b ** 2 - 2 * self.__a * self.__c

    def getRoot1(self):
        return (-self.__b + self.getDiscriminant() ** 0.5) / (2 * self.__a)

    def getRoot2(self):
        return (-self.__b - self.getDiscriminant() ** 0.5) / (2 * self.__b)


qE1 = QuadraticEquation(5, 8, 2)

print("QuadraticEquation 1")
if qE1.getDiscriminant() >= 0:
    print("\tRoot 1", qE1.getRoot1())
    print("\tRoot 2", qE1.getRoot2())
else:
    print("\tThe equation has no roots.")

qE2 = QuadraticEquation(5, 0, 2)

print("QuadraticEquation 2")
if qE2.getDiscriminant() >= 0:
    print("\tRoot 1", qE2.getRoot1())
    print("\tRoot 2", qE2.getRoot2())
else:
    print("\tThe equation has no roots.")
