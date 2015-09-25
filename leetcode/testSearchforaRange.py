__author__ = 'Brown'

import unittest
from leetcode import SearchforaRange

class MyTestCase(unittest.TestCase):
    def testSearchforaRange(self):
        self.assertEqual(SearchforaRange.Solution().searchRange([5, 7, 7, 8, 8, 10],8),[3,4],'fail')


if __name__ == '__main__':
    unittest.main()
