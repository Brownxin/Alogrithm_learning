__author__ = 'Brown'

import unittest
from leetcode import GenerateParentheses

class MyTestCase(unittest.TestCase):
    def testGenerateParentheses(self):
        self.assertEqual(GenerateParentheses.Solution().generateParenthesis(3),["((()))", "(()())", "(())()", "()(())", "()()()"],'fail')


if __name__ == '__main__':
    unittest.main()
