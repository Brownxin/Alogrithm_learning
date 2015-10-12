__author__ = 'Brown'
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.next=None
class Solution(object):
    def connect(self,root):
        if root and root.left:
            root.left.next=root.right
            if root.next:
                root.right.next=root.next.left
            else:
                root.right.next=None
        self.connect(root.left)
        self.connect(root.right)
        return root
