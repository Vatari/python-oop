# test zero
import unittest

from python_oop.iterators_and_generators.exercise.prime_numbers import get_primes


class Tests(unittest.TestCase):
    def test_zero(self):
        res = list(get_primes([2, 4, 3, 5, 6, 9, 1, 0]))
        self.assertEqual(res, [2, 3, 5])

    def test_zero(self):
        res = list(get_primes([-2, 0, 0, 1, 1, 0]))
        self.assertEqual(res, [])


if __name__ == '__main__':
    unittest.main()
