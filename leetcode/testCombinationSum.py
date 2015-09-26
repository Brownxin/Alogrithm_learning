__author__ = 'Brown'

import unittest
from leetcode import CombinationSum

class MyTestCase(unittest.TestCase):
    def testCombinationSum(self):
        self.assertEqual(CombinationSum.Solution().combinationSum([2,3,6,7],7),[[2,2,3],[7]],'fail')


if __name__ == '__main__':
    unittest.main()
