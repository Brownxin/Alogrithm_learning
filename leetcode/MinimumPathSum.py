__author__ = 'Brown'
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid==[[]]:
            return 0
        m=len(grid)
        n=len(grid[0])
        res=[[0 for j in range(n)] for i in range(m)]
        res[0][0]=grid[0][0]
        for i in range(1,m):
            res[i][0]=grid[i][0]+res[i-1][0]
        for i in range(1,n):
            res[0][i]=grid[0][i]+res[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                res[i][j]=grid[i][j]+min(res[i-1][j],res[i][j-1])
        return res[m-1][n-1]