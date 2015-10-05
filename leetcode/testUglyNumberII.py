__author__ = 'Brown'

import unittest
from leetcode import UglyNumberII

class MyTestCase(unittest.TestCase):
    def testUglyNumberII(self):
        self.assertEqual(UglyNumberII.Solution().nthUglyNumber(10),12,'fail')


if __name__ == '__main__':
    unittest.main()
