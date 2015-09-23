__author__ = 'Brown'

import unittest
from leetcode import RemoveDuplicatesfromSortedArray

class MyTestCase(unittest.TestCase):
    def testRemoveDuplicatesfromSortedArray(self):
        self.assertEqual(RemoveDuplicatesfromSortedArray.Solution().removeDuplicates([1,1,1,2,2,3]),3,'Fail')


if __name__ == '__main__':
    unittest.main()
