from math import sqrt
def get_primes(nums):
    for num in nums:
        if num <2:
            continue
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num


# test zero
import unittest

class Tests(unittest.TestCase):
    def test_zero(self):
        res = list(get_primes([2, 4, 3, 5, 6, 9, 1, 0]))
        self.assertEqual(res, [2, 3, 5])

if __name__ == '__main__':
    unittest.main()
