__author__ = 'Brown'

import unittest
from leetcode import Triangle

class MyTestCase(unittest.TestCase):
    def testTriangle(self):
        self.assertEqual(Triangle.Solution().minimumTotal([[2],
                                                        [3,4],
                                                       [6,5,7],
                                                      [4,1,8,3]]),11,'fail')


if __name__ == '__main__':
    unittest.main()
