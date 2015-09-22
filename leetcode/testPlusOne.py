__author__ = 'Brown'

import unittest
from leetcode import PlusOne

class MyTestCase(unittest.TestCase):
    def testPlusOne(self):
        self.assertEqual(PlusOne.Solution().plusOne([1,2,4]),[1,2,5],'Fail')
        self.assertEqual(PlusOne.Solution().plusOne([9,9,9]),[1,0,0,0],'Fail')
        self.assertEqual(PlusOne.Solution().plusOne([2,9,9]),[3,0,0],'Fail')

if __name__ == '__main__':
    unittest.main()
