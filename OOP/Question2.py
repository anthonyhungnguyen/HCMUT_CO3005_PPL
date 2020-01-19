class Rational:
    def __init__(self, n=0, d=1):
        assert (d != 0)
        self.__g = self.__gcd(abs(n), abs(d))
        self.numer = int(n / self.__g)
        self.denom = int(d / self.__g)

    def __gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.__gcd(b, a % b)

    def __str__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, that):
        targetType = type(that).__name__
        if targetType == 'int':
            return self.addRational(Rational(that))
        elif targetType == 'Rational':
            return self.addRational(that)

    def addRational(self, that):
        assert (type(that).__name__ == 'Rational')
        return Rational(self.numer * that.denom + self.denom * that.numer,
                        self.denom * that.denom)


x = Rational(5, 6)
y = Rational(10, 11)
print(x)
print(x + y)
