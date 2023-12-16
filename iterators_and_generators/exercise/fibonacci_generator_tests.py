# test zero
import unittest

from python_oop.iterators_and_generators.exercise.fibonacci_generator import fibonacci


class FibonacciTests(unittest.TestCase):
    def test_zero(self):
        numbers = [0, 1, 1, 2, 3]
        generator = fibonacci()
        for i in range(5):
            self.assertEqual(next(generator), numbers[i])


if __name__ == '__main__':
    unittest.main()
