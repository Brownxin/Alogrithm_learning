__author__ = 'Brown'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack=[]
        node=root
        while node:
            stack.append(node)
            node=node.left
        x=0
        while stack!=[] and x<k:
            node=stack.pop()
            right=node.right
            x+=1
            while right:
                stack.append(right)
                right=right.left
        return node.val