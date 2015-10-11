__author__ = 'Brown'
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def createBST(self,nums):
        if len(nums)==0:
            return None
        low=0
        high=len(nums)-1
        mid=low+int((high-low)/2)
        root=TreeNode(nums[mid])
        root.left=self.createBST(nums[:mid])
        root.right=self.createBST(nums[mid+1:])
        return root
    def sortedArrayToBST(self,nums):
        return self.createBST(nums)