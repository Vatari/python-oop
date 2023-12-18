# test zero
import unittest

from python_oop.iterators_and_generators.exercise.take_skip import take_skip


class TakeSkipTests(unittest.TestCase):
    def test_zero(self):
        numbers = take_skip(2, 6)
        res = []
        for number in numbers:
            res.append(number)
        self.assertEqual(res, [0, 2, 4, 6, 8, 10])


if __name__ == '__main__':
    unittest.main()
