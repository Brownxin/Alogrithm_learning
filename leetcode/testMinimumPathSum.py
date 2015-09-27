__author__ = 'Brown'

import unittest
from leetcode import MinimumPathSum

class MyTestCase(unittest.TestCase):
    def testMinimumSizeSubarraySum(self):
        self.assertEqual(MinimumPathSum.Solution().minPathSum([[1,2],[1,2]]),4,'fail')


if __name__ == '__main__':
    unittest.main()
