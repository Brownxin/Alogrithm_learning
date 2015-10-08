__author__ = 'Brown'
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 2
        if nums==[]:
            return 0
        odd=even=0
        for i in range(len(nums)):
            if i%2==0:
                even=max(even+nums[i],odd)
            else:
                odd=max(odd+nums[i],even)
        return max(even,odd)

        # Solution 1
        # if nums==[]:
        #     return 0
        # length=len(nums)
        # dp=[0 for i in range(length+1)]
        # dp[1]=nums[0]
        # for i in range(2,length+1):
        #     dp[i]=max(dp[i-1],dp[i-2]+nums[i-1])
        # return dp[length]