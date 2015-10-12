__author__ = 'Brown'
from _testcapi import INT_MAX,INT_MIN
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Solution(object):
    def dfs(self,root,min,max):
        if root==None:
            return True
        if root.val>=max or root.val<=min:
            return False
        return self.dfs(root.left,min,root.val) and self.dfs(root.right,root.val,max)
    def isValidBST(self,root):
        if root==None:
            return True
        return self.dfs(root,INT_MIN,INT_MAX)