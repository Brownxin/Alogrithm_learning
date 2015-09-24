__author__ = 'Brown'

import unittest
from leetcode import MergeSortedArray

class MyTestCase(unittest.TestCase):
    def testMergeSortedArray(self):
        self.assertEqual(MergeSortedArray.Solution().merge([2,3,5,None,None,None,None],3,[1,4,6,7],4),[1,2,3,4,5,6,7],'fail')


if __name__ == '__main__':
    unittest.main()
