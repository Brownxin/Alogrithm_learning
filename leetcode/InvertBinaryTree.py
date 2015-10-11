__author__ = 'Brown'
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    # Solution 2
    def invertTree(self,root):
        if root==None:
            return None
        queue=[root]
        while queue:
            front=queue.pop()
            if front.left:
                queue+=front.left,
            if front.right:
                queue+=front.right,
            front.left,front.right=front.right,front.left
        return root
    # Solution 1
    # def invertTree(self,root):
    #     if root==None:
    #         return None
    #     if root.left:
    #         self.invertTree(root.left)
    #     if root.right:
    #         self.invertTree(root.right)
    #     root.left,root.right=root.right,root.left
    #     return root