__author__ = 'Brown'

import unittest
from leetcode import MoveZeroes

class MyTestCase(unittest.TestCase):
    def testMoveZeroes(self):
        self.assertEqual(MoveZeroes.Solution().moveZeroes(None),None,'Fail')
        self.assertEqual(MoveZeroes.Solution().moveZeroes([]),None,'Fail')
        self.assertEqual(MoveZeroes.Solution().moveZeroes([0,2,5,0,0,4]),[2,5,4,0,0,0],'Fail')

if __name__ == '__main__':
    unittest.main()
