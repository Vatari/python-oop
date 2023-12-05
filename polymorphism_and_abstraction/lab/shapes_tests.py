# test circle
import unittest

from python_oop.polymorphism_and_abstraction.lab.shapes import Circle, Rectangle


class ShapesTests(unittest.TestCase):
    def test(self):
        c = Circle(5)
        self.assertEqual(c.calculate_area(), 78.53981633974483)
        self.assertEqual(c.calculate_perimeter(), 31.41592653589793)

    def test(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.calculate_perimeter(), 60)
        self.assertEqual(r.calculate_area(), 200)


if __name__ == "__main__":
    unittest.main()
