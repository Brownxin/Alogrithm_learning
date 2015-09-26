__author__ = 'Brown'

import unittest
from leetcode import CombinationSumII

class MyTestCase(unittest.TestCase):
    def testCombinationSumII(self):
        self.assertEqual(CombinationSumII.Solution().combinationSum2([10,1,2,7,6,1,5],8),[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],'fail')


if __name__ == '__main__':
    unittest.main()
