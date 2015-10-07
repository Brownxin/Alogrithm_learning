__author__ = 'Brown'

import unittest
from leetcode import RestoreIPAddresses

class MyTestCase(unittest.TestCase):
    def testRestoreIPAddresses(self):
        self.assertEqual(RestoreIPAddresses.Solution().restoreIpAddresses("25525511135"),["255.255.11.135", "255.255.111.35"],'fail')


if __name__ == '__main__':
    unittest.main()
