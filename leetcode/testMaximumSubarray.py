__author__ = 'Brown'

import unittest
from leetcode import MaximumSubarray

class MyTestCase(unittest.TestCase):
    def testMaximumSubarray(self):
        self.assertEqual(MaximumSubarray.Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]),6,'fail')


if __name__ == '__main__':
    unittest.main()
