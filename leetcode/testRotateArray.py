__author__ = 'Brown'

import unittest
from leetcode import RotateArray

class MyTestCase(unittest.TestCase):
    def testRotateArray(self):
        self.assertEqual(RotateArray.Solution().rotate([1],0),[1],'Fail' )
        self.assertEqual(RotateArray.Solution().rotate([1,2],1),[2,1],'Fail' )


if __name__ == '__main__':
    unittest.main()
