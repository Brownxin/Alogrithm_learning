__author__ = 'Brown'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getNode(self,root,mid_path,length):
        while root and length>0:
            length-=1
            if (mid_path & (1<<(length))):
                root=root.right
            else:
                root=root.left
        return root
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        length=0
        node=root
        while node!=None:
            node=node.left
            length+=1
        left=0
        right=(1<<(length-1))-1
        while left<=right:
            mid=(left+right)>>1
            if self.getNode(root,mid,length-1):
                left=mid+1
            else:
                right=mid-1
        return (1<<(length-1))+right



