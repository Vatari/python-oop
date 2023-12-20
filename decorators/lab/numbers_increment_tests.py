# test zero
import unittest

from python_oop.decorators.lab.number_increment import number_increment


class NumberIncrementTests(unittest.TestCase):
    def test_zero(self):
        result = number_increment([1, 2, 3])
        self.assertEqual(result, [2, 3, 4])


if __name__ == "__main__":
    unittest.main()
