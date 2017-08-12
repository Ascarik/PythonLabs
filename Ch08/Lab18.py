import math


class Circle2D:
    def __init__(self, x=0.0, y=0.0, radius=0.0):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__x

    def get_radius(self) -> float:
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_area(self) -> float:
        return math.pi * self.__radius ** 2

    def get_perimeter(self) -> float:
        return math.pi * self.__radius * 2

    def containsPoint(self, x, y) -> bool:
        return ((self.__x - x) ** 2 + (self.__y - y) ** 2) ** 0.5 < self.__radius

    def __distance(self, p) -> float:
        return ((self.__x - p.get_x()) ** 2 + (self.__y - p.get_y()) ** 2) ** 0.5

    def contains(self, circle) -> bool:
        return self.__distance(circle) <= math.fabs(self.__radius - circle.get_radius())

    def overlaps(self, circle) -> bool:
        return self.__distance(circle) < (circle.get_radius() + self.__radius) \
               and not self.contains(circle)

    def __contains__(self, another) -> bool:
        return self.contains(another)

    # _ _cmp_ _, _ _lt_ _, _ _le_ _, _ _eq_ _, _ _ne_ _, _ _gt_ _, _ _ge_ _

    def __cmp__(self, other) -> int:
        change = self.get_radius() - other.get_radius()
        if change < 0:
            return -1
        elif change == 0:
            return 0
        else:
            return 1

    def __lt__(self, other) -> bool:
        return self.get_radius() < other.get_radius()

    def __le__(self, other) -> bool:
        return self.get_radius() <= other.get_radius()

    def __eq__(self, other) -> bool:
        return self.get_radius() == other.get_radius()

    def __ne__(self, other) -> bool:
        return self.get_radius() != other.get_radius()

    def __gt__(self, other) -> bool:
        return self.get_radius() > other.get_radius()

    def __ge__(self, other) -> bool:
        return self.get_radius() >= other.get_radius()


if __name__ == '__main__':
    x1, y1, radius1 = 5, 5.5, 10
    x2, y2, radius2 = 9, 1.3, 10

    c1 = Circle2D(x1, y1, radius1)
    c2 = Circle2D(x2, y2, radius2)
    print("Area for c1 is", c1.get_area())
    print("Perimeter for c1 is", c1.get_perimeter())
    print("Area for c2 is", c2.get_area())
    print("Perimeter for c2 is", c1.get_perimeter())

    print("c1 contains the center of c2?", c1.containsPoint(c2.get_x(), c2.get_y()))
    print("c1 contains c2?", c1.contains(c2))
    print("c1 overlaps c2?", c1.overlaps(c2))
