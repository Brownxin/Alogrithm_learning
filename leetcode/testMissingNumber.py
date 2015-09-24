__author__ = 'Brown'

import unittest
from leetcode import MissingNumber

class MyTestCase(unittest.TestCase):
    def testMissingNumber(self):
        self.assertEqual(MissingNumber.Solution().missingNumber([0,1,2,3,5,6]),4,'fail')


if __name__ == '__main__':
    unittest.main()
