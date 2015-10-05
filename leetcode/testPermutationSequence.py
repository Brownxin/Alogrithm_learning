__author__ = 'Brown'

import unittest
from leetcode import PermutationSequence

class MyTestCase(unittest.TestCase):
    def testPermutationSequence(self):
        self.assertEqual(PermutationSequence.Solution().getPermutation(8,3),["123",
"132",
"213",
"231",
"312",
"321"],'fail')


if __name__ == '__main__':
    unittest.main()
