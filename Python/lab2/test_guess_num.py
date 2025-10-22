import unittest
from guess_num import guess_number


class TestGuessNum(unittest.TestCase):
    def test_1(self):
        target = 5
        nums = list(range(1, 6))
        method = 'slow'
        self.assertEqual(guess_number(target, nums, method), (5, 5))

    def test_2(self):
        target = 1
        nums = list(range(1, 6))
        method = 'slow'
        self.assertEqual(guess_number(target, nums, method), (1, 1))

    def test_3(self):
        target = 2
        nums = list(range(1, 6))
        method = 'slow'
        self.assertEqual(guess_number(target, nums, method), (2, 2))

    def test_4(self):
        target = 5
        nums = list(range(1, 6))
        method = 'binary'
        self.assertEqual(guess_number(target, nums, method), (5, 3))

    def test_5(self):
        target = 1
        nums = list(range(1, 6))
        method = 'binary'
        self.assertEqual(guess_number(target, nums, method), (1, 2))

    def test_6(self):
        target = 2
        nums = list(range(1, 6))
        method = 'binary'
        self.assertEqual(guess_number(target, nums, method), (2, 3))


if __name__ == '__main__':
    unittest.main()
