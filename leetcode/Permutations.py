__author__ = 'Brown'
class Solution(object):
    def permute(self,nums):
        if nums==[]:
            return nums
        def dfs(depth,nums,list):
            if depth==len(nums):
                res.append(list)
                return
            for i in range(len(nums)):
                if not nums[i] in list:
                    dfs(depth+1,nums,list+[nums[i]])
        res=[]
        dfs(0,nums,[])
        return res
