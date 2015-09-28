__author__ = 'Brown'

import unittest
from leetcode import FindtheDuplicateNumber

class MyTestCase(unittest.TestCase):
    def testFindtheDuplicateNumber(self):
        self.assertEqual(FindtheDuplicateNumber.Solution().findDuplicate([1,2,3,4,4,5,6]),4,'fail')


if __name__ == '__main__':
    unittest.main()
