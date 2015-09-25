__author__ = 'Brown'

import unittest
from  leetcode import RotateImage

class MyTestCase(unittest.TestCase):
    def testRotateImage(self):
        self.assertEqual(RotateImage.Solution().rotate([[1,2],[3,4]]),[[3,1],[4,2]],'fail')


if __name__ == '__main__':
    unittest.main()
