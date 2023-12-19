# test zero
import unittest

from python_oop.decorators.lab.even_numbers import even_numbers


class EvenNumbersTests(unittest.TestCase):
    def test_zero(self):
        @even_numbers
        def get_numbers(numbers):
            return numbers

        self.assertEqual(get_numbers([1, 2, 3, 4, 5]), [2, 4])


if __name__ == "__main__":
    unittest.main()
