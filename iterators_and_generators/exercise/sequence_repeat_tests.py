# test zero
import unittest

from python_oop.iterators_and_generators.exercise.sequence_repeat import sequence_repeat


class Tests(unittest.TestCase):
    def test_zero(self):
        result = list(sequence_repeat('abc', 5))
        self.assertEqual(result, ['a', 'b', 'c', 'a', 'b'])


if __name__ == '__main__':
    unittest.main()
