__author__ = 'Brown'

import unittest
from leetcode import IntegertoRoman

class MyTestCase(unittest.TestCase):
    def testIntegertoRoman(self):
        self.assertEqual(IntegertoRoman.Solution().intToRoman(24),'XXIV','fail')


if __name__ == '__main__':
    unittest.main()
