__author__ = 'Brown'

import unittest
from leetcode import JumpGame

class MyTestCase(unittest.TestCase):
    def testJumpGame(self):
        self.assertEqual(JumpGame.Solution().canJump([2,3,1,1,4]),True,'fail')
        self.assertEqual(JumpGame.Solution().canJump([3,2,1,0,4]),False,'fail')


if __name__ == '__main__':
    unittest.main()
