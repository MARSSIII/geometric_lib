import math
import unittest


class CircleTestCase(unittest.TestCase):

    """
    Class of tests for Trinagle.py func
    :param: unittest (TestCase) parent class
    """

    def test_Circle_AreaOfZero(self):

        """
        case:
        Test func(Area) for zero values
        """

        self.assertRaises(ValueError, area, 0)

    def test_Circle_AreaIntValue(self):

        """
        case:
        Test func(Area) for int values
        """

        result = area(5)
        self.assertEquals(result, math.pi * 5 * 5)

    def test_Circle_AreaOfNegative(self):

        """
        case:
        Test func(Area) for Negative values
        """

        self.assertRaises(ValueError, area, -3)

    def test_Circle_PerimeterOfZero(self):

        """
        case:
        Test func(Perimeter) for Zero values
        """

        self.assertRaises(ValueError, perimeter, 0)

    def test_Circle_PerimeterIntValues(self):

        """
        case:
        Test func(Perimeter) for int values
        """

        result = perimeter(5)
        self.assertEquals(result, 10 * math.pi)

    def test_Circle_PerimeterOfNegative(self):

        """
        case:
        Test func(perimeter) for negative values
        """

        self.assertRaises(ValueError, perimeter, -3)


def area(r):

    """
    :param r: circle radius
    :return: Circle Area(Formula: Pi * radius ^ 2
    """

    return math.pi * r * r


def perimeter(r):

    """
    :param r: circle radius
    :return: Circle Perimeter(Formula: 2 * Pi * radius
    """

    return 2 * math.pi * r
