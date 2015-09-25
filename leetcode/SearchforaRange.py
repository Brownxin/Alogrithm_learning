__author__ = 'Brown'
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low=0
        high=len(nums)-1
        while low<=high:
            mid=low+int((high-low)/2)
            if target<nums[mid]:
                high=mid-1
            if target>nums[mid]:
                low=mid+1
            if target==nums[mid]:
                start=0
                end=0
                if nums[low]==target: start=low
                if nums[high]==target: end=high
                for i in range(mid,low-1,-1):
                    if not nums[i]==target:
                        start=i+1
                        break
                for i in range(mid,high+1):
                    if not nums[i]==target:
                        end=i-1
                        break
                return [start,end]
        return [-1,-1]