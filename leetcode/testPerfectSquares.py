__author__ = 'Brown'

import unittest
from leetcode import PerfectSquares

class MyTestCase(unittest.TestCase):
    def testPerfectSquares(self):
        self.assertEqual(PerfectSquares.Solution().numSquares(13),2,'fail')


if __name__ == '__main__':
    unittest.main()
