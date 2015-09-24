__author__ = 'Brown'

import unittest
from leetcode import PascalTriangle

class MyTestCase(unittest.TestCase):
    def testPascalTriangle(self):
        self.assertEqual(PascalTriangle.Solution().generate(4),
                         [[1],
                          [1,1],
                          [1,2,1],
                          [1,3,3,1]],'Fail')


if __name__ == '__main__':
    unittest.main()
