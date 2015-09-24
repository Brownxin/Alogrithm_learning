__author__ = 'Brown'

import unittest
from leetcode import MajorityElement

class MyTestCase(unittest.TestCase):
    def testMajorityElement(self):
        self.assertEqual(MajorityElement.Solution().majorityElement([1,1,2,2]),1,'fail')


if __name__ == '__main__':
    unittest.main()
