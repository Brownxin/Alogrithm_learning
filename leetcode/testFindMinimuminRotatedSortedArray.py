__author__ = 'Brown'

import unittest
from leetcode import FindMinimuminRotatedSortedArray

class MyTestCase(unittest.TestCase):
    def testFindMinimuminRotatedSortedArray(self):
        self.assertEqual(FindMinimuminRotatedSortedArray.Solution().findMin([4,5,6,7,0,1,2]),0,'fail')


if __name__ == '__main__':
    unittest.main()
