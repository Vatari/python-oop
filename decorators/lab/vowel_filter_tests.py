# test zero
import unittest

from python_oop.decorators.lab.vowel_filter import vowel_filter


class VowelFilterTests(unittest.TestCase):
    def test_zero(self):
        @vowel_filter
        def get_letters():
            return ["a", "b", "c", "d", "e"]

        res = get_letters()
        self.assertEqual(res, ["a", "e"])


if __name__ == "__main__":
    unittest.main()
