__author__ = 'Brown'

import unittest
from leetcode import MinimumSizeSubarraySum

class MyTestCase(unittest.TestCase):
    def testMinimumSizeSubarraySum(self):
        self.assertEqual(MinimumSizeSubarraySum.Solution().minSubArrayLen(7,[2,3,1,2,4,3]),2,'fail')


if __name__ == '__main__':
    unittest.main()
