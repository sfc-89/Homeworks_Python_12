from PR_8_Yura_Fedotov import Fraction


def tests():
    # Test _simplify
    assert Fraction(2, 4) == Fraction(1, 2)

    # Test printout
    assert Fraction(1, 2).printout() == "1/2"

    # Test get_int
    assert Fraction(5, 4).get_int() == [1, Fraction(1, 4)]
    assert Fraction(3, 4).get_int() == [0, Fraction(3, 4)]

    # Test convert
    assert Fraction(5, 4).convert() == 1.25

    # Test fracture
    assert Fraction.fracture(0.25) == Fraction(1, 4)

    # Test 0 numerator
    assert Fraction(0, 2) == 0

    # Test adding:
    assert Fraction(1, 2) + Fraction(1, 4) == Fraction(3, 4)
    assert Fraction(1, 2) + 1 == Fraction(3, 2)
    assert Fraction(1, 2) + 0.25 == Fraction(3, 4)

    # Test sub:
    assert Fraction(1, 2) - Fraction(1, 4) == Fraction(1, 4)
    assert Fraction(1, 2) - 1 == Fraction(-1, 2)
    assert Fraction(1, 2) - 0.25 == Fraction(1, 4)

    # Test truediv:
    assert Fraction(1, 2) / Fraction(1, 2) == Fraction(2, 2)
    assert Fraction(1, 2) / 0.5 == Fraction(2, 2)
    assert Fraction(1, 2) / 2 == Fraction(1, 4)

    # Test mul:
    assert Fraction(1, 2) * Fraction(1, 2) == Fraction(1, 4)
    assert Fraction(1, 2) * 2 == 1
    assert Fraction(1, 2) * 0.5 == 0.25

    # Test lt:
    assert Fraction(1, 2) > Fraction(1, 4)
    assert Fraction(1, 2) > 0.25
    assert Fraction(3, 2) > 1

    # Test gt:
    assert Fraction(1, 2) < Fraction(3, 4)
    assert Fraction(1, 2) < 1.25
    assert Fraction(3, 2) < 2

    # Test eq:
    assert Fraction(1, 2) == Fraction(2, 4)
    assert Fraction(1, 2) == 0.5
    assert Fraction(2, 2) == 1

if __name__ == '__main__':
    tests()
