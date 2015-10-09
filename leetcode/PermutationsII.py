__author__ = 'Brown'
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length=len(nums)
        if length==0:
            return []
        if length==1:
            return [nums]
        nums.sort()
        res=[]
        previous=None
        for i in range(length):
            if previous==nums[i]:
                continue
            previous=nums[i]
            for j in self.permuteUnique(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+j)
        return res
