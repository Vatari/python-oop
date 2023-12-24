# test first zero
import unittest

from python_oop.decorators.exercise.type_check import type_check


class TypeCheckTests(unittest.TestCase):
    def test_zero_first(self):
        @type_check(int)
        def times2(num):
            return num * 2

        self.assertEqual(times2(2), 4)
        self.assertEqual(times2('Not A Number'), 'Bad Type')

    def test_zero_second(self):
        @type_check(str)
        def first_letter(word):
            return word[0]

        self.assertEqual(first_letter('Hello World'), 'H')
        self.assertEqual(first_letter(['Not', 'A', 'String']), 'Bad Type')


if __name__ == '__main__':
    unittest.main()
