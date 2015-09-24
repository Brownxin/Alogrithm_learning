__author__ = 'Brown'
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums==None or nums==[]:
            return None
        p=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[p],nums[i]=nums[i],nums[p]
                p+=1
        return nums