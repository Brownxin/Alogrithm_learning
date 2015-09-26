__author__ = 'Brown'

import unittest
from leetcode import UniquePaths

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(UniquePaths.Solution().uniquePaths(2,2),2,'fail')


if __name__ == '__main__':
    unittest.main()
