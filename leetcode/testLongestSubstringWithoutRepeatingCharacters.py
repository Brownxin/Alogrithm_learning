__author__ = 'Brown'

import unittest
from leetcode import LongestSubstringWithoutRepeatingCharacters

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(LongestSubstringWithoutRepeatingCharacters.Solution().lengthOfLongestSubstring('abacdfaagbc'),5,'fail')


if __name__ == '__main__':
    unittest.main()
