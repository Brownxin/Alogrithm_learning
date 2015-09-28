__author__ = 'Brown'

import unittest
from leetcode import SpiralMatrix

class MyTestCase(unittest.TestCase):
    def testSpiralMatrix(self):
        self.assertEqual(SpiralMatrix.Solution().spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]),[1,2,3,6,9,8,7,4,5],'fail')


if __name__ == '__main__':
    unittest.main()
