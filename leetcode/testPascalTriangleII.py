__author__ = 'Brown'

import unittest
from leetcode import PascalTriangleII

class MyTestCase(unittest.TestCase):
    def testPascalTriangleII(self):
        self.assertEqual(PascalTriangleII.Solution().getRow(4),[1,4,6,4,1],"fail")


if __name__ == '__main__':
    unittest.main()
