# test zero
import unittest

from python_oop.decorators.exercise.logged import logged


class LoggedTests(unittest.TestCase):
    def test_zero(self):
        @logged
        def func(*args):
            return 3 + len(args)

        result = func(4, 4, 4)
        self.assertEqual(result, 'you called func(4, 4, 4)\nit returned 6')

    def test_zero_second(self):
        @logged
        def sum_func(a, b):
            return a + b

        result = sum_func(1, 4)
        self.assertEqual(result, 'you called sum_func(1, 4)\nit returned 5')


if __name__ == '__main__':
    unittest.main()
