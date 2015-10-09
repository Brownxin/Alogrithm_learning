__author__ = 'Brown'
class Solution:

    def maximalSquare(self,maxtrix):
        if maxtrix==[]:
            return 0
        row=len(maxtrix)
        col=len(maxtrix[0])
        dp=[[0 for j in range(col)] for i in range(row)]
        res=0
        for i in range(row):
            for j in range(col):
                dp[i][j]=int(maxtrix[i][j])
                if i!=0 and j!=0 and dp[i][j]==1:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                res=max(res,dp[i][j])
        return res*res
