# test zero
import unittest

from python_oop.iterators_and_generators.exercise.take_halves import solution


class TakeHalvesTests(unittest.TestCase):
    def test_zero(self):
        take = solution()[0]
        halves = solution()[1]
        result = take(5, halves())
        self.assertEqual(result, [0.5, 1.0, 1.5, 2.0, 2.5])


if __name__ == '__main__':
    unittest.main()
