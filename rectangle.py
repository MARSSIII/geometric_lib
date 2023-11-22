import unittest


class RectangleTestCase(unittest.TestCase):

    """
    Class of tests for Triangle.py func
    :param: unittest (TestCase) parent class
    """

    def test_Rectangle_AreaOfZero(self):

        """
        case:
        Test func(Area) for zero values
        """

        self.assertRaises(ValueError, area, 0, 1)

    def test_Rectangle_AreaIntValue(self):

        """
        case:
        Test func(Area) for int values
        """

        result = area(2, 3)
        self.assertEquals(result, 6)

    def test_Rectangle_AreaOfNegative(self):

        """
        case:
        Test func(Area) for Negative values
        """

        self.assertRaises(ValueError, area, -1, 34)

    def test_Rectangle_PerimeterOfZero(self):

        """
        case:
        Test func(Perimeter) for zero values
        """

        self.assertRaises(ValueError, perimeter, 3, 0)

    def test_Rectangle_PerimeterIntValue(self):

        """
        case:
        Test func(Perimeter) for int values
        """

        result = perimeter(5, 6)
        self.assertEquals(result, 22)

    def test_Rectangle_PerimeterNegative(self):

        """
        case:
        Test func(Perimeter) for Negative values
        """

        self.assertRaises(ValueError, perimeter, -1, 3)


def area(a, b):

    """
    :param a: side (first) of the rectangle
    :param b: side (second) of the rectangle
    :return: Rectangle Area (Formula: siae(first) * side(second))
    """

    return a * b 


def perimeter(a, b):

    """
    :param a: siae (first) of the rectangle
    :param b: side (second) of the rectangle
    :return: Rectangle Perimeter (Formula: (side(first) + side(second)) * 2)
    """

    return (a + b) * 2 
