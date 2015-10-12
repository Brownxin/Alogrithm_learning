__author__ = 'Brown'
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def flatten(self,root):
        if root==None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        p=root
        if p.left==None:
            return
        p=p.left
        while p.right:
            p=p.right
        p.right=root.right
        root.right=root.left
        root.left=None
