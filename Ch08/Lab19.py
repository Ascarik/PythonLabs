class Rectangle2D:
    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__x

    def get_width(self) -> float:
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self) -> float:
        return self.__height

    def set_height(self, height):
        self.__height = height

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_area(self) -> float:
        return self.__width * self.__height

    def get_perimeter(self) -> float:
        return (self.__width + self.__height) * 2

    def containsPoint(self, x, y) -> bool:
        xc = self.__x
        yc = self.__y
        return (xc <= x <= (xc + self.__width)) and (yc <= y <= (yc + self.__height))

    def contains(self, other) -> bool:
        xc = self.__x
        yc = self.__y
        return xc <= other.get_x() and (other.get_x() + other.get_width()) <= (xc + self.__width) \
               and yc >= other.get_y() and (other.get_y() + other.get_height()) <= (yc + self.__height)

    def overlaps(self, other) -> bool:
        xo = other.get_x()
        yo = other.get_y()
        xow = other.get_x() + other.get_width()
        yoh = other.get_y() + other.get_height()

        overlap_sum = 0

        if self.containsPoint(xo, yo):
            overlap_sum += 1

        if self.containsPoint(xo, yoh):
            overlap_sum += 1

        if self.containsPoint(xow, yoh):
            overlap_sum += 1

        if self.containsPoint(xow, yo):
            overlap_sum += 1

        return overlap_sum >= 1 and overlap_sum != 4

    def __contains__(self, another) -> bool:
        return self.contains(another)

    # # _ _cmp_ _, _ _lt_ _, _ _le_ _, _ _eq_ _, _ _ne_ _, _ _gt_ _, _ _ge_ _

    def __cmp__(self, other) -> int:
        change = self.get_area() - other.get_area()
        if change < 0:
            return -1
        elif change == 0:
            return 0
        else:
            return 1

    def __lt__(self, other) -> bool:
        return self.get_area() < other.get_area()

    def __le__(self, other) -> bool:
        return self.get_area() <= other.get_area()

    def __eq__(self, other) -> bool:
        return self.get_area() == other.get_area()

    def __ne__(self, other) -> bool:
        return self.get_area() != other.get_area()

    def __gt__(self, other) -> bool:
        return self.get_area() > other.get_area()

    def __ge__(self, other) -> bool:
        return self.get_area() >= other.get_area()


if __name__ == '__main__':
    x1, y1, width1, height1 = 9, 1.3, 10, 35.3
    x2, y2, width2, height2 = 1.3, 4.3, 4, 5.3

    r1 = Rectangle2D(x1, y1, width1, height1)
    r2 = Rectangle2D(x2, y2, width2, height2)
    print("Area for r1 is", r1.get_area())
    print("Perimeter for r1 is", r1.get_perimeter())
    print("Area for r2 is", r2.get_area())
    print("Perimeter for r2 is", r1.get_perimeter())

    print("r1 contains the center of r2?", r1.containsPoint(r2.get_x(), r2.get_y()))
    print("r1 contains r2?", r1.contains(r2))
    print("r1 overlaps r2?", r1.overlaps(r2))
