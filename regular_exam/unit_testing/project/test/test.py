import unittest
from collections import deque

from project.railway_station import RailwayStation


class TestRailwayStation(unittest.TestCase):

    def test_valid_name(self):
        station = RailwayStation("Valid Name")
        self.assertEqual(station.name, "Valid Name")

    def test_station_name_three_symbols(self):
        with self.assertRaises(ValueError) as ve:
            RailwayStation("ABC")
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")

    def test_name_less_than_3_symbols(self):
        with self.assertRaises(ValueError) as ve:
            RailwayStation("AB")
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")

    def test_empty_name(self):
        with self.assertRaises(ValueError) as ve:
            RailwayStation("")
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")

    def test_new_arrival(self):
        station = RailwayStation("Central Station")
        station.new_arrival_on_board("Train A")
        self.assertEqual(station.arrival_trains, deque(["Train A"]))

    def test_append_multiple_train_info(self):
        station = RailwayStation("Test Station")
        station.new_arrival_on_board("Train A")
        station.new_arrival_on_board("Train B")
        station.new_arrival_on_board("Train C")
        self.assertEqual(station.arrival_trains, deque(["Train A", "Train B", "Train C"]))

    def test_train_arrived_first(self):
        station = RailwayStation("Main Station")
        station.new_arrival_on_board("Train X")
        result = station.train_has_arrived("Train X")
        self.assertEqual(result, "Train X is on the platform and will leave in 5 minutes.")
        self.assertEqual(station.arrival_trains, deque([]))
        self.assertEqual(station.departure_trains, deque(["Train X"]))

    def test_train_arrived_before_other_trains(self):
        station = RailwayStation("City Station")
        station.new_arrival_on_board("Train P")
        station.new_arrival_on_board("Train Q")
        result = station.train_has_arrived("Train R")
        self.assertEqual(result, "There are other trains to arrive before Train R.")
        self.assertEqual(station.arrival_trains, deque(["Train P", "Train Q"]))
        self.assertEqual(station.departure_trains, deque([]))

    def test_is_train_left(self):
        station = RailwayStation("Express Station")
        station.new_arrival_on_board("Train Y")
        station.train_has_arrived("Train Y")
        result = station.train_has_left("Train Y")
        self.assertTrue(result)
        self.assertEqual(station.departure_trains, deque([]))

    def test_train_has_left_with_no_departure_trains(self):
        station = RailwayStation("Station")
        result = station.train_has_left("Train 1")
        self.assertFalse(result)

    def test_is_not_train_left(self):
        station = RailwayStation("Terminal Station")
        station.new_arrival_on_board("Train Z")
        station.train_has_arrived("Train Z")
        result = station.train_has_left("Train X")  # Non-existing train
        self.assertFalse(result)
        self.assertEqual(station.departure_trains, deque(["Train Z"]))


if __name__ == "__main__":
    unittest.main()
