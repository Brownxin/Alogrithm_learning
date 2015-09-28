__author__ = 'Brown'
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return None
        low=1
        high=len(nums)-1
        while low<=high:
            mid=low+int((high-low)/2)
            count=0
            for i in range(0,len(nums)):
                if nums[i]<=mid:
                    count+=1
            if count<=mid:
                low=mid+1
            else:
                high=mid-1
        return low