# test zero
import unittest

from python_oop.iterators_and_generators.exercise.reader import read_next


class Tests(unittest.TestCase):
    def test_zero(self):
        res = ''
        for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
            res += str(item)
        self.assertEqual(res, 'string2dict')


if __name__ == '__main__':
    unittest.main()
