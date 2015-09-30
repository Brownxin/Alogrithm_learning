__author__ = 'Brown'

import unittest
from leetcode import ContainerWithMostWater

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(ContainerWithMostWater.Solution().maxArea([1,2,3,4]),4,'fail')


if __name__ == '__main__':
    unittest.main()
