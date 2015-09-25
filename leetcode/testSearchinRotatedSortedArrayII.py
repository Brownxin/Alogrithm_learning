__author__ = 'Brown'

import unittest
from leetcode import SearchinRotatedSortedArrayII

class MyTestCase(unittest.TestCase):
    def testSearchinRotatedSortedArrayII(self):
        self.assertEqual(SearchinRotatedSortedArrayII.Solution().search([4,5,5,6,6,0,1,1,2,3],2),True,'fail')
        self.assertEqual(SearchinRotatedSortedArrayII.Solution().search([4,5,5,6,6,0,1,1,2,3],5),True,'fail')
        self.assertEqual(SearchinRotatedSortedArrayII.Solution().search([4,5],5),True,'fail')


if __name__ == '__main__':
    unittest.main()
