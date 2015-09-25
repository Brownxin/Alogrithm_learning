__author__ = 'Brown'

import unittest
from leetcode import SearchInsertPosition

class MyTestCase(unittest.TestCase):
    def testSearchInsertPosition(self):
        self.assertEqual(SearchInsertPosition.Solution().searchInsert([1,5,6,7,8],6),2,'fail')
        self.assertEqual(SearchInsertPosition.Solution().searchInsert([1,5,6,7,8],4),1,'fail')
        self.assertEqual(SearchInsertPosition.Solution().searchInsert([1,5,6,7,8],0),0,'fail')
        self.assertEqual(SearchInsertPosition.Solution().searchInsert([1],0),0,'fail')
        self.assertEqual(SearchInsertPosition.Solution().searchInsert([1,3],1),0,'fail')


if __name__ == '__main__':
    unittest.main()
