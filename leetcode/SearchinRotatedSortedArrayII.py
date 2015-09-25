__author__ = 'Brown'

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums==[]: return False
        if len(nums)==1:
            if nums[0]==target: return True
        low=0
        high=len(nums)-1
        if len(nums)>2:
            while low+1<high:
                mid=low+int((high-low)/2)
                if target==nums[mid]: return True
                elif nums[low]==nums[mid]==nums[high]:
                    low+=1
                    high-=1
                elif nums[mid]>=nums[low]:
                    if target>=nums[low] and target<nums[mid]:
                        high=mid
                    else:
                        low=mid
                else:
                    if target<=nums[high] and target>nums[mid]:
                        low=mid
                    else:
                        high=mid
        if target==nums[low] or target==nums[high]: return True
        return False
