__author__ = 'Brown'

import unittest
from leetcode import BestTimetoBuyandSellStockII

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(BestTimetoBuyandSellStockII.Solution().maxProfit([2,1]),0,'fail')


if __name__ == '__main__':
    unittest.main()
