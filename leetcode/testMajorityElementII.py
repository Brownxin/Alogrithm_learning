__author__ = 'Brown'

import unittest
from leetcode import MajorityElementII

class MyTestCase(unittest.TestCase):
    def testMajorityElementII(self):
        self.assertEqual(MajorityElementII.Solution().majorityElement([2,1,1,2,3,1,1,2,2,3]),[1,2],'fail')


if __name__ == '__main__':
    unittest.main()
