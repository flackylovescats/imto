import unittest
from bin_tree import gen_bin_tree

class TestBinTree(unittest.TestCase):
    def test_tree_2_2(self):
        height = 2
        root = 2
        self.assertEqual(gen_bin_tree(height, root), {'root': 2, 'left': {'root': 4}, 'right': {'root': 6}})  # add assertion here

    def test_tree_3_3(self):
        height = 3
        root = 3
        self.assertEqual(gen_bin_tree(height, root), {'root': 3, 'left': {'root': 5, 'left': {'root': 7}, 'right': {'root': 15}}, 'right': {'root': 9, 'left': {'root': 11}, 'right': {'root': 27}}})

if __name__ == '__main__':
    unittest.main()
