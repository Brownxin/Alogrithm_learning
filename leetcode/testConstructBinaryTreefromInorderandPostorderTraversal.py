__author__ = 'Brown'

import unittest
from leetcode import ConstructBinaryTreefromInorderandPostorderTraversal

class MyTestCase(unittest.TestCase):
    def testConstructBinaryTreefromInorderandPostorderTraversal(self):
        n=ConstructBinaryTreefromInorderandPostorderTraversal.TreeNode(1)
        n.left=ConstructBinaryTreefromInorderandPostorderTraversal.TreeNode(2)
        n.right=None
        self.assertEqual(ConstructBinaryTreefromInorderandPostorderTraversal.Solution().buildTree([1,2],[2,1]),n,'fail')


if __name__ == '__main__':
    unittest.main()
