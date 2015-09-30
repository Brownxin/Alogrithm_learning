__author__ = 'Brown'
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return None
        if len(nums)==1:
            return nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            res=res^nums[i]
        return res