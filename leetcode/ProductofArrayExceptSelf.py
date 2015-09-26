__author__ = 'Brown'
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[1 for i in range(len(nums))]
        left=1
        right=1
        for i in range(1,len(nums)):
            left*=nums[i-1]
            res[i]*=left
        for i in range(len(nums)-2,-1,-1):
            right*=nums[i+1]
            res[i]*=right
        return res