__author__ = 'Brown'
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums==[]:
            return 0
        if len(nums)==1:
            if target<=nums[0]: return 0
            else: return 1
        low=0
        high=len(nums)-1
        if len(nums)>2:
            while low+1<high:
                mid=low+int((high-low)/2)
                if target==nums[mid]:
                    return mid
                elif target>nums[mid]:
                    low=mid
                else:
                    high=mid
        if target<=nums[low]: return low
        elif target>nums[high]: return high+1
        else: return low+1