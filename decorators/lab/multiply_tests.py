# test zero
import unittest

from python_oop.decorators.lab.multiply import multiply


class MultiplyTests(unittest.TestCase):
    def test_zero(self):
        @multiply(3)
        def add_ten(number):
            return number + 10

        self.assertEqual(add_ten(3), 39)

    def test_zero_second(self):
        @multiply(5)
        def add_ten(number):
            return number + 10

        self.assertEqual(add_ten(6), 80)


if __name__ == "__main__":
    unittest.main()
