# test car
import unittest

from python_oop.polymorphism_and_abstraction.exercise.vehicles import Car, Truck


class VehiclesTests(unittest.TestCase):
    def test_first_zero(self):
        car = Car(20, 5)
        car.drive(3)
        self.assertEqual(car.fuel_quantity, 2.299999999999997)
        car.refuel(10)
        self.assertEqual(car.fuel_quantity, 12.299999999999997)

    def test_second_zero(self):
        truck = Truck(100, 15)
        truck.drive(5)
        self.assertEqual(truck.fuel_quantity, 17.0)
        truck.refuel(50)
        self.assertEqual(truck.fuel_quantity, 64.5)


if __name__ == '__main__':
    unittest.main()
