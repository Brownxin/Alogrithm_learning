__author__ = 'Brown'

import unittest
from leetcode import SpiralMatrixII

class MyTestCase(unittest.TestCase):
    def testSpiralMatrixII(self):
        self.assertEqual(SpiralMatrixII.Solution().generateMatrix(3),[[ 1, 2, 3 ],[ 8, 9, 4 ],[ 7, 6, 5 ]],'fail')


if __name__ == '__main__':
    unittest.main()
