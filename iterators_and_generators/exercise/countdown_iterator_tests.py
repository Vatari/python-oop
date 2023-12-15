# test zero
import unittest

from python_oop.iterators_and_generators.exercise.countdown_iterator import countdown_iterator


class CountdownIteratorTests(unittest.TestCase):
    def test_zero(self):
        iterator = countdown_iterator(10)
        result = []
        for item in iterator:
            result.append(item)
        self.assertEqual(result, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])


if __name__ == '__main__':
    unittest.main()
