__author__ = 'Brown'
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def preorderTraversal(self,root):
        res=[]
        stack=[]
        while root or stack:
            if root:
                stack.append(root)
                res.append(root.val)
                root=root.left
            else:
                root=stack.pop()
                root=root.right
        return res