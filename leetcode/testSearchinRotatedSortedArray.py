__author__ = 'Brown'

import unittest
from leetcode import SearchinRotatedSortedArray

class MyTestCase(unittest.TestCase):
    def testSearchinRotatedSortedArray(self):
        self.assertEqual(SearchinRotatedSortedArray.Solution().search([4,5,6,7,0,1,2,3],6),2,'fail')


if __name__ == '__main__':
    unittest.main()
