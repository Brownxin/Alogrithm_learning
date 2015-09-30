__author__ = 'Brown'

import unittest
from leetcode import H_Index

class MyTestCase(unittest.TestCase):
    def testH_Index(self):
        self.assertEqual(H_Index.Solution().hIndex([3, 0, 6, 1, 5]),3,'fail')


if __name__ == '__main__':
    unittest.main()
