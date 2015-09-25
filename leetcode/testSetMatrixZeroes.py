__author__ = 'Brown'

import unittest
from leetcode import SetMatrixZeroes

class MyTestCase(unittest.TestCase):
    def testSetMatrixZeroes(self):
        self.assertEqual(SetMatrixZeroes.Solution().setZeroes([[1,0,1],
                                                               [0,1,1],
                                                               [1,1,1],
                                                               [1,1,1]]),[[0,0,0],
                                                                          [0,0,0],
                                                                          [0,0,1],
                                                                          [0,0,1]],'fail')


if __name__ == '__main__':
    unittest.main()
