__author__ = 'Brown'

import unittest
from leetcode import NextPermutation

class MyTestCase(unittest.TestCase):
    def testNextPermutation(self):
        self.assertEqual(NextPermutation.Solution().nextPermutation([1,3,2]),[2,1,3],'fail')
        self.assertEqual(NextPermutation.Solution().nextPermutation([3,2,1]),[1,2,3],'fail')


if __name__ == '__main__':
    unittest.main()
