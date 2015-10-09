__author__ = 'Brown'
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    def dfs(self,nums):
        if len(nums)==0:
            return [None]
        res=[]
        for root_index in range(len(nums)):
            left=self.dfs(nums[:root_index])
            right=self.dfs(nums[root_index+1:])
            for l in left:
                for r in right:
                    root=TreeNode(nums[root_index])
                    root.left=l
                    root.right=r
                    res.append(root)
        return res

    def generateTrees(self,n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # if n==1:
        #     return [TreeNode(1)]
        return self.dfs([i for i in range(1,n+1)])