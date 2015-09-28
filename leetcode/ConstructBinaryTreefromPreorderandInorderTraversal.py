__author__ = 'Brown'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return None
        root=preorder.pop(0)
        node=TreeNode(root)
        index=inorder.index(root)
        node.left=self.buildTree(preorder,inorder[:index])
        node.right=self.buildTree(preorder,inorder[index+1:])
        return node