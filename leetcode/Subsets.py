__author__ = 'Brown'
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []

        res=[]
        def dfs(depth,start,list):
            if not list in res:
                res.append(list)
            if depth==len(nums):
                return
            for i in range(start,len(nums)):
                dfs(depth+1,i+1,list+[nums[i]])
        nums.sort()
        dfs(0,0,[])
        return res