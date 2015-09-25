__author__ = 'Brown'
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums==[]:
            return -1
        if len(nums)==1:
            if nums[0]==target: return 0
        low=0
        high=len(nums)-1
        if len(nums)>2:
            while low+1<high:
                mid=low+int((high-low)/2)
                if nums[mid]==target:
                    return mid
                elif nums[mid]>=nums[low]:
                    if target>=nums[low] and target<nums[mid]:
                        high=mid
                    else:
                        low=mid
                elif nums[mid]<nums[high]:
                    if target>nums[mid] and target<=nums[high]:
                        low=mid
                    else:
                        high=mid
        if nums[low]==target: return low
        if nums[high]==target: return high
        return -1
