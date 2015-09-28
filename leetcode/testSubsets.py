__author__ = 'Brown'

import unittest
from leetcode import Subsets

class MyTestCase(unittest.TestCase):
    def testSubsets(self):
        self.assertEqual(Subsets.Solution().subsets([1,2,3]),[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]],'fail')


if __name__ == '__main__':
    unittest.main()

[[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]