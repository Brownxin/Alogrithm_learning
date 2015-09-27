__author__ = 'Brown'
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        res=[[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i]==1:
                break
            res[0][i]=1
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0]==1:
                break
            res[i][0]=1
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                if obstacleGrid[i][j]==0:
                    res[i][j]=res[i-1][j]+res[i][j-1]
        return res[len(obstacleGrid)-1][len(obstacleGrid[0])-1]