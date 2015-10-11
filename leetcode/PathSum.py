__author__ = 'Brown'
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def hasPathSum(self,root,sum):
        if root==None:
            return False
        if root.left==None or root.right==None:
            return root.val==sum
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)