__author__ = 'Brown'
import unittest
from leetcode import Permutations
class MyTestCase(unittest.TestCase):
    def testPermutations(self):
        self.assertEqual(Permutations.Solution().permute([1,2,3]),[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2],[3,2,1]],'fail')

if __name__=='__main__':
    unittest.main()