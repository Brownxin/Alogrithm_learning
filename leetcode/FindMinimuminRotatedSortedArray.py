__author__ = 'Brown'
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return None
        low=0
        high=len(nums)-1
        while nums[low]>nums[high]:
            mid=low+int((high-low)/2)
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid-1
        return nums[low]

        # Solution 1
        # if len(nums)==0:
        #     return None
        # low=0
        # high=len(nums)-1
        # while low<high:
        #     mid=low+int((high-low)/2)
        #     if nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]:
        #         return nums[mid]
        #     elif nums[mid]>nums[high]:
        #         low=mid+1
        #     elif nums[mid]<nums[low]:
        #         high=mid-1
        #     elif nums[mid]<nums[mid+1] and nums[mid]>nums[mid-1]:
        #         return nums[low]
        # return nums[low]
