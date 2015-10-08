__author__ = 'Brown'

import unittest
from leetcode import SimplifyPath

class MyTestCase(unittest.TestCase):
    def testSimplifyPath(self):
        self.assertEqual(SimplifyPath.Solution().simplifyPath("/a/./b/../../c/"),"/c",'fail')


if __name__ == '__main__':
    unittest.main()
