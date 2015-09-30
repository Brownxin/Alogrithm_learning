__author__ = 'Brown'

import unittest
from leetcode import _3SumClosest

class MyTestCase(unittest.TestCase):
    def test_3SumClosest(self):
        self.assertEqual(_3SumClosest.Solution().threeSumClosest([-1,2,1,-4],1),2,'fail')


if __name__ == '__main__':
    unittest.main()
