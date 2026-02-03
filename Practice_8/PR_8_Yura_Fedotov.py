import math


class Fraction:
    def __init__(self, numerator, denominator):
        self._is_exists(x=numerator, y=denominator)
        self.__GCD: int = math.gcd(numerator, denominator)
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

    def __add__(self, other):
        """a/b + c/d"""
        lcm: int = math.lcm(self.denominator, other.denominator)
        return Fraction(
            numerator=(self.numerator * (lcm // self.denominator) + other.numerator * (lcm // other.denominator)),
            denominator=lcm
        )

    def __sub__(self, other):
        """a/b - c/d"""
        lcm: int = math.lcm(self.denominator, other.denominator)
        return Fraction(
            numerator=(self.numerator * (lcm // self.denominator) - other.numerator * (lcm // other.denominator)),
            denominator=lcm
        )

    def __truediv__(self, other):
        """a/b / c/d"""
        return Fraction(
            numerator=self.numerator * other.denominator,
            denominator=self.denominator * other.numerator
        )

    def __mul__(self, other):
        """a/b * c/d"""
        return Fraction(
            numerator=self.numerator * other.numerator,
            denominator=self.denominator * other.denominator
        )

    def __lt__(self, other) -> bool:
        """a/b < c/d"""
        if not isinstance(other, Fraction):
            return NotImplemented
        lcm = math.lcm(self.denominator, other.denominator)
        return self.numerator * (lcm // self.denominator) < other.numerator * (lcm // other.denominator)

    def __gt__(self, other):
        """a/b > c/d"""
        if not isinstance(other, Fraction):
            return NotImplemented
        lcm = math.lcm(self.denominator, other.denominator)
        return self.numerator * (lcm // self.denominator) > other.numerator * (lcm // other.denominator)

    def __eq__(self, other):
        """a/b == c/d"""
        if not isinstance(other, Fraction):
            return NotImplemented
        lcm = math.lcm(self.denominator, other.denominator)
        return self.numerator * (lcm // self.denominator) == other.numerator * (lcm // other.denominator)

    def __mod__(self, other):
        """a/b % c/d"""
        return Fraction

    def __pow__(self, other):
        """a/b ** c/d"""
        return Fraction


if __name__ == '__main__':
    pass