__author__ = 'Brown'
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 1
        dp=[0 for i in range(n+1)]
        dp[1]=dp[0]=1
        for step in range(2,n+1):
            dp[step]=dp[step-1]+dp[step-2]
        return dp[n]