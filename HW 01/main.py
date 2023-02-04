import unittest
import math

def classify_triangle(a, b, c):
    """ Function that classifies triangle based on given values """
    type = ""
    # All sides are equal -> Equilateral triangle
    if a == b and a == c and b == c:
        type = "Equilateral triangle"
    # Any two sides are equal -> Isosceles triangle
    elif a == b or a == c or b == c:
        type = "Isosceles triangle"
    # No equal sides -> Scalene triangle
    else:
        type = "Scalene triangle"
    # Checking for right angle triangle
    if (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b):
        type += " & right angle triangle"
    else:
        type += " & not a right angle triangle"
    return type


class TestMyBrand(unittest.TestCase):
    def test_classify_triangle(self):
        self.assertEqual(classify_triangle(2, 2, 4), "Isosceles triangle & not a right angle triangle")
        self.assertEqual(classify_triangle(2, 2, 2), "Equilateral triangle & not a right angle triangle")
        self.assertEqual(classify_triangle(2, 3, 4), "Scalene triangle & not a right angle triangle")
        self.assertEqual(classify_triangle(5, 3, 4), "Scalene triangle & right angle triangle")


unittest.main(argv=[''], verbosity=1, exit=False);
