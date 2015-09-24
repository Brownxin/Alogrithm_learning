__author__ = 'Brown'

import unittest
from leetcode import SortColors

class MyTestCase(unittest.TestCase):
    def testSortColors(self):
        self.assertEqual(SortColors.Solution().sortColors([0,1,2,2,2,1,0,0,1]),[0,0,0,1,1,1,2,2,2],'fail')
        self.assertEqual(SortColors.Solution().sortColors([0,1,0,0,1]),[0,0,0,1,1],'fail')


if __name__ == '__main__':
    unittest.main()
