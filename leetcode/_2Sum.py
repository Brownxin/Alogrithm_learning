__author__ = 'Brown'
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Solution 1
        # if len(nums)<2:
        #     return None,None
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return i+1,j+1

        # Solution 2
        dict={}
        for i in range(len(nums)):
            dict[target-nums[i]]=i
        for i in range(len(nums)):
            if nums[i] in dict and i<dict[nums[i]]:
                return i+1,dict[nums[i]]+1