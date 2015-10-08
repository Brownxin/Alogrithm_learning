__author__ = 'Brown'

import unittest
from leetcode import ReverseWordsinaString

class MyTestCase(unittest.TestCase):
    def testReverseWordsinaString(self):
        self.assertEqual(ReverseWordsinaString.Solution().reverseWords('the sky is blue'),'blue is sky the','fail')


if __name__ == '__main__':
    unittest.main()
