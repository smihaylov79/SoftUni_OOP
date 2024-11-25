from unittest import TestCase, main
from collections import deque

from project.railway_station import RailwayStation

class TestRailwayStation(TestCase):
    name='Varna'
    arrival_trains=deque(['666', '444'])
    departure_trains = deque(['111', '222'])

    def setUp(self):
        self.railway_station = RailwayStation(self.name)

    def test_init(self):
        self.assertIsInstance(self.railway_station.arrival_trains, deque)
        self.assertIsInstance(self.railway_station.departure_trains, deque)
        self.assertEqual(self.name, self.railway_station.name)
        self.assertIsInstance(self.railway_station.name, str)

    def test_property_of_name(self):

        with self.assertRaises(ValueError) as context:
            self.railway_station.name = 'a'
        self.assertEqual("Name should be more than 3 symbols!", str(context.exception))

    def test_new_arrival_trains(self):
        self.railway_station.new_arrival_on_board('555')
        self.assertIn('555', self.railway_station.arrival_trains)

    def test_arrived_fail(self):
        self.railway_station.arrival_trains = self.arrival_trains
        result= self.railway_station.train_has_arrived('666')
        self.assertEqual("There are other trains to arrive before 666.", result)

    def test_arrival_success(self):
        self.railway_station.arrival_trains = self.arrival_trains
        result = self.railway_station.train_has_arrived('666')
        self.assertEqual("666 is on the platform and will leave in 5 minutes.", result)
        self.assertNotIn('666', self.railway_station.arrival_trains)
        self.assertIn('666', self.railway_station.departure_trains)

    def test_train_left_success(self):
        self.railway_station.departure_trains = self.departure_trains
        result= self.railway_station.train_has_left('111')
        self.assertEqual(False, result)

    def test_train_left_fail(self):
        self.railway_station.departure_trains = self.departure_trains
        result= self.railway_station.train_has_left('111')
        self.assertEqual(True, result)




if __name__ == '__main__':
    main()