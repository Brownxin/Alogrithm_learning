__author__ = 'Brown'

import unittest
from leetcode import SingleNumber

class MyTestCase(unittest.TestCase):
    def testSingleNumber(self):
        self.assertEqual(SingleNumber.Solution().singleNumber([1,2,3,4,4,5,2,3,1]),5,'fail')


if __name__ == '__main__':
    unittest.main()
