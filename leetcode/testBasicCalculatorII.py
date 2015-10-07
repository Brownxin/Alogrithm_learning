__author__ = 'Brown'

import unittest
from leetcode import BasicCalculatorII

class MyTestCase(unittest.TestCase):
    def testBasicCalculatorII(self):
        self.assertEqual(BasicCalculatorII.Solution().calculate(" 3+5 / 2 "),5,'fail')


if __name__ == '__main__':
    unittest.main()
