__author__ = 'Brown'
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0 for i in range(n+1)]
        dp[0]=1
        for k in range(1,n+1):
            for left in range(k):
                dp[k]+=dp[left]*dp[k-1-left]
        return dp[n]