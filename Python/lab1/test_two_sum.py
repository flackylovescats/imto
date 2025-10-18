import unittest
from two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(two_sum(nums, target), [0, 1])

    def test_2(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(two_sum(nums, target), [1, 2])

    def test_3(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(two_sum(nums, target), [0, 1])


if __name__ == '__main__':
    unittest.main()
