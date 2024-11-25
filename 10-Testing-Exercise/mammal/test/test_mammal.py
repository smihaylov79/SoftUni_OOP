from unittest import TestCase, main

from project.mammal import Mammal


class MammalTest(TestCase):

    def setUp(self):
        self.mammal = Mammal('Test', 'test type', 'test sound')

    def init_test(self):
        self.assertEqual('Test', self.mammal.name)
        self.assertEqual('test type', self.mammal.type)
        self.assertEqual('test sound', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result=self.mammal.make_sound()
        self.assertEqual('Test makes test sound', result)

    def test_get_kingdom(self):
        result=self.mammal.get_kingdom()
        self.assertEqual('animals', result)

    def test_info(self):
        self.assertEqual('Test is of type test type', self.mammal.info())


if __name__ == '__main__':
    main()
