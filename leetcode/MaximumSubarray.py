__author__ = 'Brown'
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=-10*10
        cur_sum=0
        for i in range(len(nums)):
            if cur_sum<0:
                cur_sum=0
            cur_sum+=nums[i]
            max_sum=max(max_sum,cur_sum)
        return max_sum