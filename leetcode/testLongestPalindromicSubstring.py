__author__ = 'Brown'

import unittest
from leetcode import LongestPalindromicSubstring

class MyTestCase(unittest.TestCase):
    def testLongestPalindromicSubstring(self):
        self.assertEqual(LongestPalindromicSubstring.Solution().longestPalindrome('1234567898765432567765'),'234567898765432','fail')


if __name__ == '__main__':
    unittest.main()
