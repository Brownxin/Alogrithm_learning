__author__ = 'Brown'
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def getHeight(self,root):
        if root==None:
            return 0
        return max(self.getHeight(root.left),self.getHeight(root.right))+1
    def isBalanced(self,root):
        if root==None:
            return True
        if abs(self.getHeight(root.left)-self.getHeight(root.right))<=1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else: return False