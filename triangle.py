import unittest


class TriangleTestCase(unittest.TestCase):

    """
    Class of tests for Triangle.py func
    :param: unittest(Testcase) parent class
    """

    def test_Triangle_AreaOfZero(self):

        """
        case:
        Test func(Area) for zero values
        """

        self.assertRaises(ValueError, area, 0, 3)

    def test_Triangle_AreaIntValue(self):

        """
        case:
        Test func(Area) for int values
        """

        result = area(10, 4)
        self.assertEquals(result, 20)

    def test_Triangle_AreaOfNegative(self):

        """
        case:
        Test func(Area) for Negative values
        """

        self.assertRaises(ValueError, area, -1, 4)

    def test_Triangle_PerimeterOfZero(self):

        """
        case:
        Test func(Perimeter) for Zero values
        """

        self.assertRaises(ValueError, perimeter, 0, 3, 2)

    def test_Triangle_PerimeterIntValue(self):

        """
        case:
        Test func(Perimeter) for Int Values
        """

        result = perimeter(1, 3, 4)
        self.assertEquals(result, 8)

    def test_Triangle_PerimeterOfNegative(self):

        """
        case:
        Test func(Perimeter) for Negative Values
        """

        self.assertRaises(ValueError, perimeter, -1, 2, 3)


def area(a, h):

    """
    :param a: side triangle
    :param h: height triangle
    :return: Triangle Area (Formula: a * h / 2)
    """

    return a * h / 2 


def perimeter(a, b, c):

    """
    :param a: side(first) triangle
    :param b: side(second) triangle
    :param c: side(third) triangle
    :return: Triangle perimeter (Formula: side(firts) + side(second) + side(third )
    """

    return a + b + c 
