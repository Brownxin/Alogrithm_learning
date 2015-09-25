__author__ = 'Brown'

import unittest
from leetcode import BestTimetoBuyandSellStock

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(BestTimetoBuyandSellStock.Solution().maxProfit([5,6,10,2,3,8]),6,'fail')


if __name__ == '__main__':
    unittest.main()
