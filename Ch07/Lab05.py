import math


class RegularPolygon:
    def __init__(self, n=3, side=1, x=0.0, y=0.0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def getN(self):
        return self.__n

    def setN(self, n):
        self.__n = n

    def getSide(self):
        return self.__side

    def setSide(self, side):
        self.__side = side

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y

    def getPerimeter(self):
        return self.__side * self.__n

    def getArea(self):
        return self.__n * math.pow(self.__side, 2) / (4 * math.tan(math.pi / self.__n))


# RegularPolygon(),
# using RegularPolygon(6, 4) and RegularPolygon(10, 4, 5.6, 7.8)

poly1 = RegularPolygon()
poly2 = RegularPolygon(6, 4)
poly3 = RegularPolygon(10, 4, 5.6, 7.8)

print("Poly 1\n\t primeter is {}\n\t area is {}".format(poly1.getPerimeter(), poly1.getArea()))
print("Poly 2\n\t primeter is {}\n\t area is {}".format(poly2.getPerimeter(), poly2.getArea()))
