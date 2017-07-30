class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getD(self):
        return self.__d

    def getE(self):
        return self.__e

    def getF(self):
        return self.__f

    def setA(self, a):
        self.__a = a

    def setB(self, b):
        self.__b = b

    def setC(self, c):
        self.__c = c

    def setD(self, d):
        self.__d = d

    def setE(self, e):
        self.__e = e

    def setF(self, f):
        self.__f = f

    def isSolvable(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0

    def getX(self):
        return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)

    def getY(self):
        return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)


lE = LinearEquation(5, 2, 6, 5, 4, 3)

if lE.isSolvable() == 0:
    print("The equation has no solution.")
else:
    print("x =", lE.getX())
    print("y =", lE.getY())
