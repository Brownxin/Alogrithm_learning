__author__ = 'Brown'

import unittest
from leetcode import RemoveElement


class MyTestCase(unittest.TestCase):
    def testRemoveElement(self):
        self.assertEqual(RemoveElement.Solution().removeElement([1,1,1,1,1,3,3,4,4],1),4,'Fail')
        self.assertEqual(RemoveElement.Solution().removeElement([],1),0,'Fail')

if __name__ == '__main__':
    unittest.main()
