__author__ = 'Brown'

import unittest
from leetcode import RemoveDuplicatesfromSortedArrayII

class MyTestCase(unittest.TestCase):
    def testRemoveDuplicatesfromSortedArrayII(self):
        self.assertEqual(RemoveDuplicatesfromSortedArrayII.Solution().removeDuplicates([1,1,2,2,2,2,3,4,4,4]),7,'fail')


if __name__ == '__main__':
    unittest.main()
