__author__ = 'Brown'

import unittest
from leetcode import Searcha2DMatrix

class MyTestCase(unittest.TestCase):
    def testSearcha2DMatrix(self):
        self.assertEqual(Searcha2DMatrix.Solution().searchMatrix([[1,   3,  5,  7],
                                                                  [10, 11, 16, 20],
                                                                  [23, 30, 34, 50]],3),True,'fail')


if __name__ == '__main__':
    unittest.main()
