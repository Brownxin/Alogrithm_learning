__author__ = 'Brown'

import unittest
from leetcode import WordSearch

class MyTestCase(unittest.TestCase):
    def testWordSearch(self):
        # self.assertEqual(WordSearch.Solution().exist([["ABCE"],["SFCS"],["ADEE"]],'SEE'),True,'fail')
        self.assertEqual(WordSearch.Solution().exist([["ABCE"],["SFCS"],["ADEE"]],'ABAB'),False,'fail')


if __name__ == '__main__':
    unittest.main()
