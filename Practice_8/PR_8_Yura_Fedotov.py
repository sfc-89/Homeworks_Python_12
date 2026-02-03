import math
from functools import wraps


class Fraction:
    def __init__(self, numerator, denominator):
        self._is_exists(x=numerator, y=denominator)
        self.__GCD: int = math.gcd(numerator, denominator)
        self._simplify(numerator, denominator)

    def printout(self):
        return f"{self.numerator}/{self.denominator}"

    def _simplify(self, x: int, y: int) -> None:
        self.numerator = int(x / self.__GCD)
        self.denominator = int(y / self.__GCD)

    @staticmethod
    def check_other_number(func):
        """Check if other value is a number, if yes - converts number to Fraction"""
        @wraps(func)
        def wrapper(self, other):
            if isinstance(other, (int, float)):
                return func(self, Fraction.fracture(other))
            elif isinstance(other, Fraction):
                return func(self, other)
            return NotImplemented

        return wrapper

    def get_int(self) -> list[int | object]:
        """returns an [integer, remainder]"""
        temp_numerator = self.numerator
        result = 0
        while temp_numerator >= self.denominator:
            temp_numerator -= self.denominator
            result += 1
        return [result, Fraction(temp_numerator, self.denominator)]

    def convert(self):
        """Converts from fraction to float"""
        return self.numerator / self.denominator

    @staticmethod
    def fracture(other):
        """Converts a number to fraction"""
        if isinstance(other, int):
            return Fraction(numerator=other, denominator=1)

        elif isinstance(other, float):
            number_splited: list[str] = str(other).split('.')
            if number_splited[1] == '0':
                return Fraction(numerator=int(number_splited[0]), denominator=1)
            else:
                return (Fraction(
                    denominator=10 ** len(number_splited[1]),
                    numerator=int(number_splited[1]) + int(number_splited[0]) * 10 ** len(number_splited[1])
                ))
        else:
            raise ValueError("Not a number")

    @staticmethod
    def _is_exists(x: int, y: int):
        """Inner: check if fraction exists"""
        if y == 0:
            raise ZeroDivisionError("Denominator cannot be 0")
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Numerator and Denominator must be numbers")

    @check_other_number
    def __add__(self, other):
        """a/b + c/d"""
        lcm: int = math.lcm(self.denominator, other.denominator)
        return Fraction(
            numerator=(self.numerator * (lcm // self.denominator) + other.numerator * (lcm // other.denominator)),
            denominator=lcm
        )

    @check_other_number
    def __sub__(self, other):
        """a/b - c/d"""
        lcm: int = math.lcm(self.denominator, other.denominator)
        return Fraction(
            numerator=(self.numerator * (lcm // self.denominator) - other.numerator * (lcm // other.denominator)),
            denominator=lcm
        )

    @check_other_number
    def __truediv__(self, other):
        """a/b / c/d"""
        return Fraction(
            numerator=self.numerator * other.denominator,
            denominator=self.denominator * other.numerator
        )

    @check_other_number
    def __mul__(self, other):
        """a/b * c/d"""
        return Fraction(
            numerator=self.numerator * other.numerator,
            denominator=self.denominator * other.denominator
        )

    @check_other_number
    def __lt__(self, other) -> bool:
        """a/b < c/d"""
        lcm: int = math.lcm(self.denominator, other.denominator)
        return self.numerator * (lcm // self.denominator) < other.numerator * (lcm // other.denominator)

    @check_other_number
    def __gt__(self, other):
        """a/b > c/d"""
        lcm: int = math.lcm(self.denominator, other.denominator)
        return self.numerator * (lcm // self.denominator) > other.numerator * (lcm // other.denominator)

    @check_other_number
    def __eq__(self, other):
        """a/b == c/d"""
        lcm: int = math.lcm(self.denominator, other.denominator)
        return self.numerator * (lcm // self.denominator) == other.numerator * (lcm // other.denominator)


if __name__ == '__main__':
    pass