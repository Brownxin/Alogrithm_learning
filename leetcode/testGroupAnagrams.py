__author__ = 'Brown'

import unittest
from leetcode import GroupAnagrams

class MyTestCase(unittest.TestCase):
    def testGroupAnagrams(self):
        self.assertEqual(GroupAnagrams.Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),[["ate", "eat","tea"],["nat","tan"],["bat"]],'fail')


if __name__ == '__main__':
    unittest.main()
