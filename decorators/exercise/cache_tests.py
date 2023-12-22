# test first zero
import unittest

from python_oop.decorators.exercise.cache import cache


class CacheTests(unittest.TestCase):
    def test_zero_first(self):
        @cache
        def fibonacci(n):
            if n < 2:
                return n
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)

        fibonacci(3)
        self.assertEqual(fibonacci.log, {1: 1, 0: 0, 2: 1, 3: 2})

    def test_zero_second(self):
        @cache
        def fibonacci(n):
            if n < 2:
                return n
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)

        fibonacci(4)
        self.assertEqual(fibonacci.log, {1: 1, 0: 0, 2: 1, 3: 2, 4: 3})


if __name__ == '__main__':
    unittest.main()
