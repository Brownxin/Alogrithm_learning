__author__ = 'Brown'
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def LowestCommonAncestor(self,root,p,q):
        while (p.val-root.val)*(q.val-root.val)>0:
            root=[root.left,root.right][p.val>root.val]
        return root