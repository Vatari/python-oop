# test zero
import unittest

from python_oop.iterators_and_generators.exercise.possible_permutations import possible_permutations


class Tests(unittest.TestCase):
    def test_zero(self):
        result = possible_permutations([1, 2, 3])
        self.assertEqual(next(result), [1, 2, 3])
        self.assertEqual(next(result), [1, 3, 2])
        self.assertEqual(next(result), [2, 1, 3])
        self.assertEqual(next(result), [2, 3, 1])
        self.assertEqual(next(result), [3, 1, 2])
        self.assertEqual(next(result), [3, 2, 1])

    def test_zero_2(self):
        result = possible_permutations([1])
        self.assertEqual(next(result), [1])
        with self.assertRaises(StopIteration):
            next(result)


if __name__ == '__main__':
    unittest.main()
