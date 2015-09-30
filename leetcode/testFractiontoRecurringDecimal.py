__author__ = 'Brown'

import unittest
from leetcode import FractiontoRecurringDecimal

class MyTestCase(unittest.TestCase):
    def testFractiontoRecurringDecimal(self):
        self.assertEqual(FractiontoRecurringDecimal.Solution().fractionToDecimal(11,3),'3.(6)','fail')


if __name__ == '__main__':
    unittest.main()
