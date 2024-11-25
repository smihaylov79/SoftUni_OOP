from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTest(TestCase):
    fuel=3.5
    horse_power=100.0

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_class_attributes(self):
        self.assertIsInstance(self.vehicle.fuel, float)
        self.assertIsInstance(self.vehicle.horse_power, float)

    def test_drive_success(self):
        self.vehicle.drive(2)
        self.assertEqual(1, self.vehicle.fuel)

    def test_drive_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(5)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_success(self):
        self.vehicle.fuel=1
        self.vehicle.refuel(1.2)
        self.assertEqual(2.2, self.vehicle.fuel)

    def test_refuel_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(5)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        expected="The vehicle has 100.0 horse power with 3.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, str(self.vehicle))



if __name__ == '__main__':
    main()