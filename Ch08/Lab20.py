class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        n = self.numerator
        d = self.denominator

        return Rational(n * other.denominator + other.numerator * d, d * other.denominator)

    def __str__(self):
        return "numerator = {}, denominator={}".format(self.numerator, self.denominator)


if __name__ == '__main__':
    sum = Rational(0, 1)
    for i in range(1, 10, 1):
        sum += Rational(i, i + 1)

    print(sum)
