# test first zero
import unittest

from python_oop.decorators.exercise.HTML_tags import tags


class TagsTests(unittest.TestCase):
    def test_zero_first(self):
        @tags('p')
        def join_strings(*args):
            return "".join(args)

        self.assertEqual(join_strings("Hello", " you!"), '<p>Hello you!</p>')

    def test_zero_second(self):
        @tags('h1')
        def to_upper(text):
            return text.upper()

        self.assertEqual(to_upper('hello'), '<h1>HELLO</h1>')


if __name__ == '__main__':
    unittest.main()
