class Intersection:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.__x1 = x1
        self.__x2 = x2
        self.__x3 = x3
        self.__x4 = x4
        self.__y1 = y1
        self.__y2 = y2
        self.__y3 = y3
        self.__y4 = y4

    def getX(self):
        return ((self.__x1 * self.__y2 - self.__y1 * self.__x2) * (self.__x3 - self.__x4) - (self.__x1 - self.__x2) \
                * (self.__x3 * self.__y4 - self.__y3 * self.__x4)) \
               / ((self.__x1 - self.__x2) * (self.__y3 - self.__y4) - (self.__y1 - self.__y2) * (self.__x3 - self.__x4))

    def getY(self):
        return ((self.__x1 * self.__y2 - self.__y1 * self.__x2) * (self.__y3 - self.__y4) - (self.__y1 - self.__y2) \
                * (self.__x3 * self.__y4 - self.__y3 * self.__x4)) \
               / ((self.__x1 - self.__x2) * (self.__y3 - self.__y4) - (self.__y1 - self.__y2) * (self.__x3 - self.__x4))


x1, y1, x2, y2 = eval(input("Enter the endpoints of the first line segment"))
x3, y3, x4, y4 = eval(input("Enter the endpoints of the second line segment"))
# x1, y1, x2, y2 = 2.0, 2.0, 0, 0
# x3, y3, x4, y4 = 0, 2.0, 2.0, 0

i = Intersection(x1, y1, x2, y2, x3, y3, x4, y4)
print("The intersecting point is: ({}, {})".format(i.getX(), i.getY()))
