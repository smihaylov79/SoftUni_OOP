from unittest import TestCase, main

# from Test_Worker import Worker


class WorkerTests(TestCase):
    def test_init(self):
        w = Worker("Test", 1000, 100)
        self.assertEqual(w.name, "Test")
        self.assertEqual(w.salary, 1000)
        self.assertEqual(w.energy, 100)
        self.assertEqual(w.money, 0)

    def test_worker_work_no_energy_raises(self):
        w = Worker("Test", 1000, 0)
        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 0)

        with self.assertRaises(Exception) as exception:
            w.work()

        self.assertEqual(str(exception.exception), "Not enough energy.")

    def test_worker_works(self):
        w = Worker("Test", 1000, 100)
        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 100)

        result = w.work()
        self.assertEqual(w.money, 1000)
        self.assertEqual(w.energy, 99)
        self.assertIsNone(result)

    def test_worker_rest(self):
        w = Worker("Test", 1000, 100)
        self.assertEqual(w.energy, 100)
        result = w.rest()
        self.assertEqual(w.energy, 101)
        self.assertIsNone(result)

    def test_info(self):
        w = Worker("Test", 1000, 100)

        result = w.get_info()
        exp_res = "Test has saved 0 money."
        self.assertEqual(exp_res, result)


if __name__ == "__main__":
    main()
