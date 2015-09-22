__author__ = 'Brown'

import unittest
from leetcode import ContainsDuplicate

class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testContainsDuplicate(self):
        self.assertEqual(ContainsDuplicate.Solution().containsDuplicate([2,1,4,5]),False,'Fail!')
        self.assertEqual(ContainsDuplicate.Solution().containsDuplicate([2,1,4,5,1]),True,'Fail!')

if __name__ == '__main__':
    unittest.main()
