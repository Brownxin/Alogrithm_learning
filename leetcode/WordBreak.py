__author__ = 'Brown'
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp=[False for i in range(len(s)+1)]
        dp[0]=True
        for i in range(len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i]=True
        return dp[len(s)]