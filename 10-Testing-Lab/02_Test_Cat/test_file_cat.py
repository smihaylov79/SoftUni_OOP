from unittest import TestCase, main

from Test_Cat import Cat

class CatTests(TestCase):
    def test_init(self):
        c=Cat("Test")

        self.assertEqual(c.name, "Test")
        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)
        self.assertEqual(c.size, 0)



if __name__ == '__main__':
    main()