class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def distance(self, p) -> float:
        return ((self.__x - p.get_x()) ** 2 + (self.__y - p.get_y()) ** 2) ** 0.5

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def isNearBy(self, p):
        return True if self.distance(p) <= 5 else False

    def __str__(self):
        return "x ={0}, y={1}".format(self.__x, self.__y)


if __name__ == '__main__':
    x1, y1, x2, y2 = 2.1, 2.3, 19.1, 19.2

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    print("The distance between the two points is {:.2f}".format(p1.distance(p2)))
    if p1.isNearBy(p2):
        print("The two points are near each other")
    else:
        print("The two points are not near each other")

    x1, y1, x2, y2 = 2.1, 2.3, 2.3, 4.2

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    print("\n\nThe distance between the two points is {:.2f}".format(p1.distance(p2)))
    if p1.isNearBy(p2):
        print("The two points are near each other")
    else:
        print("The two points are not near each other")
