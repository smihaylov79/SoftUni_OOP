from unittest import TestCase, main

from extended_list import IntegerList

class IntegerListTests(TestCase):
    def test_init_stores_only_int(self):
        i= IntegerList()
        self.assertEqual(i._IntegerList__data, [])

        i = IntegerList(1, 'dfdf', 5.8, 12,'rt')
        self.assertEqual(i._IntegerList__data, [1,12])








if __name__ == '__main__':
    main()