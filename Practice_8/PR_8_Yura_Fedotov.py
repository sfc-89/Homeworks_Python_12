import math


class Fraction:
    def __init__(self, numerator, denominator):
        self._is_exists(x=numerator, y=denominator)
        self._simplify(x=numerator, y=denominator)

    def _simplify(self, x, y):
        gcd = math.gcd(x, y)
        self.numerator = int(x / gcd)
        self.denominator = int(y / gcd)

    @classmethod
    def _is_exists(cls, x, y):
        """check if fraction exists"""
        if y == 0:
            raise ZeroDivisionError("Denominator cannot be 0")
        if isinstance(x, int) or isinstance(y, int):
            raise ValueError("Numerator and Denominator must be numbers")

    def lcm(self):
        pass

    def __add__(self, other):
        """a/b + c/d"""
        return Fraction

    def __sub__(self, other):
        """a/b - c/d"""
        return Fraction

    def __truediv__(self, other):
        """a/b / c/d"""
        return Fraction

    def __mul__(self, other):
        """a/b * c/d"""
        return Fraction

    def __lt__(self, other):
        """a/b < c/d"""
        return Fraction

    def __gt__(self, other):
        """a/b > c/d"""
        return Fraction

    def __eq__(self, other):
        """a/b == c/d"""
        return Fraction

    def __mod__(self, other):
        """a/b % c/d"""
        return Fraction

    def __pow__(self, other):
        """a/b ** c/d"""
        return Fraction


if __name__ == '__main__':
    pass