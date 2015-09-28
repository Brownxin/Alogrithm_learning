__author__ = 'Brown'

import unittest
from leetcode import FindPeakElement

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(FindPeakElement.Solution().findPeakElement([2,1,2,1,3,1,4]),[0,2,4,6],'fail')


if __name__ == '__main__':
    unittest.main()
