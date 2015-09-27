__author__ = 'Brown'
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        min_length=len(nums)+1
        start=end=0
        while end<len(nums):
            while sum<s and end<len(nums):
                sum+=nums[end]
                end+=1
            while start<end and sum>=s:
                min_length=min(min_length,end-start)
                sum-=nums[start]
                start+=1
        if min_length==len(nums)+1:
            min_length=0
        return min_length