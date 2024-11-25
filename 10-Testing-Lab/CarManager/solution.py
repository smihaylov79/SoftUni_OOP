from unittest import TestCase, main

from car_manager import Car

class CarTests(TestCase):
    def test_init(self):
        c = Car('Test', 'model', 2, 30)
        self.assertEqual(c.make, 'Test')
        self.assertEqual(c.model, 'model')
        self.assertEqual(c.fuel_consumption, 2)
        self.assertEqual(c.fuel_capacity, 30)
        self.assertEqual(c.fuel_amount, 0)

    def test_make_empty_raises(self):
        with self.assertRaises(Exception) as ex:
            c = Car('', 'model', 2, 0)
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")


if __name__ == '__main__':
    main()