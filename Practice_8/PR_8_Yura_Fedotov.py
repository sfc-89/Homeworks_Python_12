import math


class Fraction:
    def __init__(self, numerator, denominator):
        self._is_exists(x=numerator, y=denominator)
        self.__LCM = math.lcm(numerator, denominator)
        self.__GCD = math.gcd(numerator, denominator)
        self._simplify(numerator, denominator)

    def _simplify(self, x: int, y: int) -> None:
        self.numerator = int(x / self.__GCD)
        self.denominator = int(y / self.__GCD)

    @staticmethod
    def _is_exists(x: int, y: int):
        """check if fraction exists"""
        if y == 0:
            raise ZeroDivisionError("Denominator cannot be 0")
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Numerator and Denominator must be numbers")

    def lcm(self):
        pass

    def __add__(self, other):
        """a/b + c/d"""
        lcm: int = math.lcm(self.denominator, other.denominator)
        return Fraction(
            numerator=(self.numerator * int(lcm / self.denominator) + other.numerator * int(lcm / other.denominator)),
            denominator=lcm
        )

    def __sub__(self, other):
        """a/b - c/d"""
        lcm: int = math.lcm(self.denominator, other.denominator)
        return Fraction(
            numerator=(self.numerator * int(lcm / self.denominator) - other.numerator * int(lcm / other.denominator)),
            denominator=lcm
        )

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