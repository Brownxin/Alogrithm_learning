__author__ = 'Brown'

import unittest
from leetcode import _2Sum

class MyTestCase(unittest.TestCase):
    def test_2Sum(self):
        self.assertEqual(_2Sum.Solution().twoSum([1,5,2,7,5],10),(2,5),'fail')


if __name__ == '__main__':
    unittest.main()
