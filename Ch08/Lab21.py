class Complex:
    def __init__(self, a: float = 0.0, b: float = 0.0):
        self.__a = a
        self.__b = b
        self.__i = -1 ** 0.5

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def __add__(self, other):
        return Complex(self.__a + other.get_a(), self.__b + other.get_b())

    def __sub__(self, other):
        return Complex(self.__a - other.get_a(), self.__b - other.get_b())

    def __mul__(self, other):
        a = self.__a
        b = self.__b
        c = other.get_a()
        d = other.get_b()
        return Complex(a * c - b * d, b * c + a * d)

    def __truediv__(self, other):
        a = self.__a
        b = self.__b
        c = other.get_a()
        d = other.get_b()
        return Complex((a * c + b * d) / (c ** 2 + d ** 2), (b * c - a * d) / (c ** 2 + d ** 2))

    def __abs__(self):
        a = self.__a
        b = self.__b
        return ((a ** 2) + (b ** 2)) ** 0.5

    def __str__(self):
        if self.__b != 0:
            return "({}  +  {}i)".format(self.__a, self.__b)
        else:
            return "({})".format(self.__a)


if __name__ == '__main__':
    a, b = 3.5, 6.5
    complex1 = Complex(a, b)
    a, b = -3.5, 1
    complex2 = Complex(a, b)

    print("{0} + {1} = {2}".format(complex1, complex2, complex1 + complex2))
    print("{0} - {1} = {2}".format(complex1, complex2, complex1 - complex2))
    print("{0} * {1} = {2}".format(complex1, complex2, complex1 * complex2))
    print("{0} / {1} = {2}".format(complex1, complex2, complex1 / complex2))
    print("| {0} | = {1}".format(complex1, abs(complex1)))
