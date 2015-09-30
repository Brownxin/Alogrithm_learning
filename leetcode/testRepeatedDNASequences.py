__author__ = 'Brown'

import unittest
from leetcode import RepeatedDNASequences

class MyTestCase(unittest.TestCase):
    def testRepeatedDNASequences(self):
        self.assertEqual(RepeatedDNASequences.Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"),["AAAAACCCCC", "CCCCCAAAAA"],'fail')


if __name__ == '__main__':
    unittest.main()