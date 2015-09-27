__author__ = 'Brown'

import unittest
from leetcode import UniquePathsII

class MyTestCase(unittest.TestCase):
    def testUniquePaths(self):
        self.assertEqual(UniquePathsII.Solution().uniquePathsWithObstacles([
                                                                              [0,0,0],
                                                                              [0,1,0],
                                                                              [0,0,0]
                                                                                        ]),2,'fail')

if __name__ == '__main__':
    unittest.main()
