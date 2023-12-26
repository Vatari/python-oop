from unittest import TestCase, main

from python_oop.testing.lab.test_worker import Worker


class WorkerTests(TestCase):
    def test_worker_is_initialized_correct(self):
        # Arrange, Act
        worker = Worker("Test", 100, 10)

        # Assert
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_is_increased_after_rest(self):
        # Arrange
        worker = Worker("Test", 100, 10)

        self.assertEqual(10, worker.energy)
        # Act
        worker.rest()

        # Assert
        self.assertEqual(11, worker.energy)

    def test_worker_work_with_zero_energy_raises(self):
        # Arrange
        worker = Worker("Test", 100, 0)

        # Act, Assert
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_is_payed_after_work(self):
        # Arrange
        worker = Worker("Test", 100, 10)
        self.assertEqual(0, worker.money)

        # Act
        worker.work()

        # Assert
        self.assertEqual(100, worker.money)

        # Act
        worker.work()

        # Assert
        self.assertEqual(200, worker.money)

    def test_energy_is_decreased_after_working(self):
        # Arrange
        worker = Worker('Test', 100, 10)
        self.assertEqual(10, worker.energy)

        # Act
        worker.work()

        # Assert
        self.assertEqual(9, worker.energy)

        # Act
        worker.work()

        # Assert
        self.assertEqual(8, worker.energy)

    def test_get_info(self):
        # Arrange
        worker = Worker('Test', 100, 10)

        result = worker.get_info()
        expected = "Test has saved 0 money."

        self.assertEqual(expected, result)

        worker.work()

        result = worker.get_info()
        expected = "Test has saved 100 money."

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
