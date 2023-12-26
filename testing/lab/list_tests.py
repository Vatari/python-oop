import unittest

from python_oop.testing.lab.list import IntegerList


class TestIntegerList(unittest.TestCase):
    def setUp(self):
        # Create an IntegerList instance with initial values for testing
        self.integer_list = IntegerList(1, 2, 3, 4, 5)

    def test_initial_values(self):
        # Check if the initial values are set correctly
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3, 4, 5])

    def test_add(self):
        # Test adding a new element
        self.integer_list.add(6)
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3, 4, 5, 6])

        # Test adding a non-integer element (should raise a ValueError)
        with self.assertRaises(ValueError):
            self.integer_list.add("not an integer")

    def test_remove_index(self):
        # Test removing an element by index
        removed_element = self.integer_list.remove_index(2)
        self.assertEqual(removed_element, 3)
        self.assertEqual(self.integer_list.get_data(), [1, 2, 4, 5])

        # Test removing from an out-of-range index (should raise an IndexError)
        with self.assertRaises(IndexError):
            self.integer_list.remove_index(10)

    def test_get(self):
        # Test getting an element by index
        element = self.integer_list.get(3)
        self.assertEqual(element, 4)

        # Test getting from an out-of-range index (should raise an IndexError)
        with self.assertRaises(IndexError):
            self.integer_list.get(10)

    def test_insert(self):
        # Test inserting an element at a specific index
        self.integer_list.insert(2, 100)
        self.assertEqual(self.integer_list.get_data(), [1, 2, 100, 3, 4, 5])

        # Test inserting at an out-of-range index (should raise an IndexError)
        with self.assertRaises(IndexError):
            self.integer_list.insert(10, 50)

        # Test inserting a non-integer element (should raise a ValueError)
        with self.assertRaises(ValueError):
            self.integer_list.insert(3, "not an integer")

    def test_get_biggest(self):
        # Test getting the biggest element
        biggest_element = self.integer_list.get_biggest()
        self.assertEqual(biggest_element, 5)

    def test_get_index(self):
        # Test getting the index of an element
        index = self.integer_list.get_index(3)
        self.assertEqual(index, 2)

        # Test getting the index of a non-existing element
        with self.assertRaises(ValueError):
            self.integer_list.get_index(100)


if __name__ == '__main__':
    unittest.main()
