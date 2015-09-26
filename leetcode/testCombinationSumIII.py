__author__ = 'Brown'

import unittest
from leetcode import CombinationSumIII

class MyTestCase(unittest.TestCase):
    def testCombinationSumIII(self):
        self.assertEqual(CombinationSumIII.Solution().combinationSum3(3,7),[[1,2,4]],'fail')


if __name__ == '__main__':
    unittest.main()
