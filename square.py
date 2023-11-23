import unittest


class SquareTestCase(unittest.TestCase):

    """
    Class of tests for Square.py func
    :param: unittest(Testcase) parent class
    """

    def test_Square_AreaOfZero(self):

        """
        case:
        Test func(Area) for zero values
        """

        self.assertRaises(ValueError, area, 0)

    def test_Square_AreaIntValue(self):

        """
        case:
        Test func(Area) for int values
        """

        result = area(10)
        self.assertEquals(result, 100)

    def test_Square_AreaOfNegative(self):

        """
        case:
        Test func(Area) for Negative values
        """

        self.assertRaises(ValueError, area, -1)

    def test_Square_PerimeterOfZero(self):

        """
        case:
        Test func(Perimeter) for Zero values
        """

        self.assertRaises(ValueError, perimeter, 0)

    def test_Square_PerimeterIntValue(self):

        """
        case:
        Test func(Perimeter) for Int Values
        """

        result = perimeter(6)
        self.assertEquals(result, 24)

    def test_Square_PerimeterOfNegative(self):

        """
        case:
        Test func(Perimeter) for Negative Values
        """

        self.assertRaises(ValueError, perimeter, -1)


def area(a):

    """
    :param a: side square
    :return: Square Area (Formula: side * side)
    """

    return a * a


def perimeter(a):

    """
    :param a: side square
    :return: Square Perimeter(Formula: 4 * side)
    """

    return 4 * a
