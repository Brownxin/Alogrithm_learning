__author__ = 'Brown'

import unittest
from leetcode import MaximumProductSubarray

class MyTestCase(unittest.TestCase):
    def testMaximumProductSubarray(self):
        self.assertEqual(MaximumProductSubarray.Solution().maxProduct([2,3,-2,4]),6,'fail')

if __name__ == '__main__':
    unittest.main()
