__author__ = 'Brown'

import unittest
from leetcode import LetterCombinationsofaPhoneNumber

class MyTestCase(unittest.TestCase):
    def testLetterCombinationsofaPhoneNumber(self):
        self.assertEqual(LetterCombinationsofaPhoneNumber.Solution().letterCombinations("23"),["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
                         'fail')


if __name__ == '__main__':
    unittest.main()