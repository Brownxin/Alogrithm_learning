__author__ = 'Brown'

import unittest
from leetcode import DecodeWays

class MyTestCase(unittest.TestCase):
    def testDecodeWays(self):
        self.assertEqual(DecodeWays.Solution().numDecodings('12782612'),8,'fail')


if __name__ == '__main__':
    unittest.main()
