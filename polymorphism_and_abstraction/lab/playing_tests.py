import unittest

from python_oop.polymorphism_and_abstraction.lab.playing import start_playing


class PlayingTest(unittest.TestCase):
    def test(self):
        class Test:
            def play(self):
                return "test"

        res = start_playing(Test())
        self.assertEqual(res, "test")


if __name__ == '__main__':
    unittest.main()
