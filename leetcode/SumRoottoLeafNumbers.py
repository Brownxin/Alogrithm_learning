__author__ = 'Brown'
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def getSum(self,root,presum):
        if root==None:
            return 0
        presum=presum*10+root.val
        if root.left==None or root.right==None: return presum
        return self.getSum(root.left,presum)+self.getSum(root.right,presum)
    def sumNumbers(self,root):
        return self.getSum(root,0)