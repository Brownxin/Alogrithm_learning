__author__ = 'Brown'

import unittest
from leetcode import _3Sum

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(_3Sum.Solution().threeSum([1,0,0,-1,2,-1]),[[-1,0,1],[-1,-1,2]],'fail')


if __name__ == '__main__':
    unittest.main()
