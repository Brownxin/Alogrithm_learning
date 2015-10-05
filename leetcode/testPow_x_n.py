__author__ = 'Brown'

import unittest
from leetcode import Pow_x_n

class MyTestCase(unittest.TestCase):
    def testPow_x_n(self):
        self.assertEqual(Pow_x_n.Solution().myPow(2,2),4.0,'fail')


if __name__ == '__main__':
    unittest.main()
