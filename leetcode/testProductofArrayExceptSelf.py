__author__ = 'Brown'

import unittest
from leetcode import ProductofArrayExceptSelf

class MyTestCase(unittest.TestCase):
    def testProductofArrayExceptSelf(self):
        self.assertEqual(ProductofArrayExceptSelf.Solution().productExceptSelf([2,3,4,5]),[60,40,30,24],'fail')


if __name__ == '__main__':
    unittest.main()
