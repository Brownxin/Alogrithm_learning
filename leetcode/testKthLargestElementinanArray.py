__author__ = 'Brown'

import unittest
from leetcode import KthLargestElementinanArray

class MyTestCase(unittest.TestCase):
    def testKthLargestElementinanArray(self):
        self.assertEqual(KthLargestElementinanArray.Solution().findKthLargest([3,2,1,5,6,4],2),5,'fail')


if __name__ == '__main__':
    unittest.main()
