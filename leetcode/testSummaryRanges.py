__author__ = 'Brown'

import unittest
from leetcode import SummaryRanges

class MyTestCase(unittest.TestCase):
    def testSummaryRanges(self):
        self.assertEqual(SummaryRanges.Solution().summaryRanges([1,3,4,5,7,8,9,11,13]),["1","3->5","7->9","11","13"],"fail")
        self.assertEqual(SummaryRanges.Solution().summaryRanges([-1]),["-1"],"fail")


if __name__ == '__main__':
    unittest.main()
