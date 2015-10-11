__author__ = 'Brown'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self,root):
        if root==None:
            return []
        res=[]
        stack=[]
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                res.append(root.val)
                root=root.right
        return res

    # Solution 1
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     def inorder(root):
    #         if root==None:
    #             return
    #         root.left=self.inorderTraversal(root.left)
    #         res.append(root.val)
    #         root.right=self.inorderTraversal(root.right)
    #         return
    #     if root==None:
    #         return []
    #     res=[]
    #     inorder(root)
    #     return res